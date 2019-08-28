# -*- encoding: utf-8 -*-
# Subject to license. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, exceptions, _

import dbf
import tempfile, os, shutil
from os.path import join, dirname
import os
import zipfile
import base64
import re
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

import logging
_logger = logging.getLogger(__name__)

class ExportFile(models.Model):
    '''Export Sage 50'''
    _name = 'export_sage_50.export_file'
    _description = 'Export File For Sage 50'
    
    _order = 'date_to desc'
    
    state = fields.Selection([
            ('draft','Draft'),
            ('completed', 'Completed'),
        ], string='Status', index=True, readonly=True, default='draft',
        copy=False,
        help=" * The 'Draft' status is used when a new export is created but not yet filled.\n"
             " * The 'Completed' status is when an export has been filled and is ready for import.\n")
    
    name = fields.Char(compute="_compute_vals",store=True)
    filename = fields.Char(compute="_compute_vals",store=True)
    
    date_from = fields.Date(string="Date From", compute="_compute_vals",store=True)
    date_to = fields.Date(string="Date To", compute="_compute_vals",store=True)
    
    invoice_ids = fields.Many2many('account.invoice', 'export_sage_50_invoice_rel','export_id','invoice_id',string="Invoices",readonly=True)
    invoice_count = fields.Integer(string="Invoices Count", compute="_compute_vals",store=True)

    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env['res.company']._company_default_get('publisher.media'))
    analytic_plan = fields.Char(compute='_compute_analytic_plan')
    
    export_file = fields.Binary(attachment=True, help="This field holds the export file for Sage 50.",readonly=True)
    export_file_name = fields.Char(compute="_compute_vals")

    @api.depends('company_id')
    @api.one
    def _compute_analytic_plan(self):
        if self.company_id.sage_50_analytic_plan:
            self.analytic_plan = str('cost_' + self.company_id.sage_50_analytic_plan[0:5].lower())

    @api.depends('invoice_ids')
    @api.one
    def _compute_vals(self):
        date_from = False
        date_to = False
        for invoice in self.invoice_ids:
            if date_to == False or invoice.date >= date_to:
                date_to = invoice.date
            if date_from == False or invoice.date <= date_from:
                date_from = invoice.date
        self.date_from = date_from
        self.date_to = date_to
        self.name = 'export%s' % (date_to)
        self.filename = 'export%s.zip' % (date_to)
        self.export_file_name = 'export%s.zip' % (date_to)
        self.invoice_count = len(self.invoice_ids)
    
    @api.multi
    def action_export_all_missing(self):
        self.ensure_one()
        self.invoice_ids = self.env['account.invoice'].search([('company_id', '=', self.company_id.id), ('is_exported_to_sage_50', '=', False),('state','in',['open','paid'])])

        self._create_export_from_invoices()
        
    @api.multi
    def action_export_last_month(self):
        self.ensure_one()
        date_from = (date.today().replace(day=1) - timedelta(days=1)).replace(day=1)
        date_to = date.today().replace(day=1) - timedelta(days=1)
        
        self.invoice_ids = self.env['account.invoice'].search([('company_id', '=', self.company_id.id), ('date','<=',date_to),('date','>=',date_from),('state','in',['open','paid'])])
        self._create_export_from_invoices()
        
    @api.multi
    def action_export_last_quarter(self):
        self.ensure_one()
        date_from = ((date.today().replace(day=1) - timedelta(days=1)).replace(day=1)) - relativedelta(months=+3)
        date_to = date.today().replace(day=1) - timedelta(days=1)
        
        self.invoice_ids = self.env['account.invoice'].search([('company_id', '=', self.company_id.id), ('date','<=',date_to),('date','>=',date_from),('state','in',['open','paid'])])
        self._create_export_from_invoices()
    
    @api.multi
    def action_export_custom(self, date_from, date_to):
        self.ensure_one()
        self.invoice_ids = self.env['account.invoice'].search([('company_id', '=', self.company_id.id), ('date','<=',date_to),('date','>=',date_from),('state','in',['open','paid'])])
        self._create_export_from_invoices()
    
    @api.one
    def _create_export_from_invoices(self):

        ### DB MANAGEMENT OBJECT ###

        class DbObject:

            class DbObjectRow:
                def __init__(self, dbObject):
                    self._dbObject = dbObject
                    self._row = dbf.create_template(self._dbObject._db)

                # Special method made to use non-code-written names
                #def setAttr(self, name, value):

                def __setattr__(self, name, value):
                    if name[:1] != '_':
                        field = self._dbObject._struct[name]
                        if field['type'] == 'char':
                            #store_value = self.removeGermanSpecialChars(value)[:field['size']]
                            store_value = value[:field['size']]
                        elif field['type'] == 'date':
                            store_value = dbf.Date(value)
                        else:
                            store_value = value

                        setattr(self._row, name, store_value)

                    self.__dict__[name] = value

                def apply(self):
                    self._dbObject._db.append(self._row)

                def removeGermanSpecialChars(self, string):
                    string = string.encode('utf8')
                    string = string.replace("ë", "e")
                    string = string.replace("Ë", "E")
                    string = string.replace("ö", "oe")
                    string = string.replace("Ö", "OE")
                    string = string.replace("ü", "u")
                    string = string.replace("Ü", "u")
                    string = string.replace("ä", "ae")
                    string = string.replace("Ä", "AE")
                    string = string.replace("ß", "ss")
                    return string

            def __init__(self, filename, structure):
                self._struct = structure.copy()

                field_specs = '';
                first = True

                for field_name in self._struct:

                    field = self._struct[field_name]

                    if first:
                        first = False
                    else:
                        field_specs += '; '

                    field_specs += field_name.upper()
                    field_specs += ' '

                    if field['type'] == 'char':
                        field_specs += 'C(' + str(field['size']) + ')'
                    elif field['type'] == 'num':
                        field_specs += 'N(' + str(field['size']) + ', ' + str(field.get('precision', 0)) + ')'
                    elif field['type'] == 'date':
                        field_specs += 'D'

                self._db = dbf.Table(filename, codepage='utf8', field_specs=field_specs)
                self._db.open(mode=dbf.READ_WRITE)

            def row(self):
                return self.DbObjectRow(self)

            def close(self):
                self._db.close()

        ### DESCRIPTIONS ###

        partner_structure = {
            'cid':          {'type': 'char', 'size': 10},
            'ccustype':     {'type': 'char', 'size': 1},
            'csuptype':     {'type': 'char', 'size': 1},
            'cname1':       {'type': 'char', 'size': 100},
            'caddress1':    {'type': 'char', 'size': 100},
            'caddress2':    {'type': 'char', 'size': 100},
            'czipcode':     {'type': 'char', 'size': 10},
            'clocality':    {'type': 'char', 'size': 40},
            'ccountry':     {'type': 'char', 'size': 6},
            'cvatref':      {'type': 'char', 'size': 2},
            'cvatno':       {'type': 'char', 'size': 12},
            'cvatcat':      {'type': 'char', 'size': 1},
            'clanguage':    {'type': 'char', 'size': 2},
            'cbankno':      {'type': 'char', 'size': 19}
        }

        partner_type_list = [
            {
                'db_name': 'CUSTOMERS.DBF',
                'types': ['out_invoice', 'out_refund'],
                'ccustype': 'C',
                'csuptype': 'U',
            },
            {
                'db_name': 'SUPPLIERS.DBF',
                'types': ['in_invoice', 'in_refund'],
                'ccustype': 'U',
                'csuptype': 'S',
            }
        ]

        invoice_structure = {
            'tdbk':     {'type': 'char',  'size': 4},
            'tfyear':   {'type': 'char',  'size': 5},
            'tyear':    {'type': 'num',   'size': 4},
            'tmonth':   {'type': 'num',   'size': 2},
            'tdocno':   {'type': 'num',   'size': 10},
            'tdocdate': {'type': 'date'},
            'ttypcie':  {'type': 'char',  'size': 1},
            'tcompan':  {'type': 'char',  'size': 10},
            'tduedate': {'type': 'date'},
            'tamount':  {'type': 'num',   'size': 10, 'precision': 2},
            'tremint':  {'type': 'char',  'size': 40},
            'tremext':  {'type': 'char',  'size': 40},
            'tintmode': {'type': 'char',  'size': 1},
            'tinvvcs':  {'type': 'char',  'size': 12}
        }

        invoice_line_structure = {
            'tdbk':         {'type': 'char',  'size': 4},
            'tfyear':       {'type': 'char',  'size': 5},
            'tyear':        {'type': 'num',   'size': 4},
            'tmonth':       {'type': 'num',   'size': 2},
            'tdocno':       {'type': 'num',   'size': 10},
            'tdocline':     {'type': 'num',   'size': 5},
            'ttypeline':    {'type': 'char',  'size': 1},
            'tdocdate':     {'type': 'date'},
            'tacttype':     {'type': 'char',  'size': 1},
            'taccount':     {'type': 'char',  'size': 10},
            'tamount':      {'type': 'num',   'size': 10, 'precision': 2},
            'tbasvat':      {'type': 'num',   'size': 10, 'precision': 2},
            'tvattotamn':   {'type': 'num',   'size': 10, 'precision': 2},
            'tvatamn':      {'type': 'num',   'size': 10, 'precision': 2},
            'tvatdblamn':   {'type': 'num',   'size': 10, 'precision': 2},
            'tbaslstamn':   {'type': 'num',   'size': 10, 'precision': 2},
            'tvstored':     {'type': 'char',  'size': 10},
            'tdc':          {'type': 'char',  'size': 1},
            'trem':         {'type': 'char',  'size': 40},
        }
        analytic_header = ""
        if self.analytic_plan != False:
            invoice_line_structure[str(self.analytic_plan)] = {'type': 'char',  'size': 2}

        invoices_type_list = [
            {
                'db_header_name': 'SALES.DBF',
                'db_line_name': 'SALESL.DBF',
                'types': ['out_invoice', 'out_refund'],
                'journal': "VEN",
                'doc_type': 'C',
                'line_doc_type_invoice': 'C',
                'line_doc_type_refund': 'D',
            },
            {
                'db_header_name': 'PURCHASES.DBF',
                'db_line_name': 'PURCHASESL.DBF',
                'types': ['in_invoice', 'in_refund'],
                'journal': "ACH",
                'doc_type': 'S',
                'line_doc_type_invoice': 'D',
                'line_doc_type_refund': 'C',
            },
        ]

        ### DB CREATION ###

        tmpdir = tempfile.mkdtemp()
        shutil.copy(join(dirname(__file__),"BOBLINK.TXT"), tmpdir)
        
        # PARTNERS

        for partner_type in partner_type_list:

            db = DbObject(join(tmpdir, partner_type['db_name']), partner_structure)

            partner_ids_id = []

            for invoice in self.invoice_ids:
                if invoice.type in partner_type['types']:
                    if not invoice.partner_id.id in partner_ids_id:
                        partner_ids_id.append(invoice.partner_id.id)

            partner_ids = self.env['res.partner'].search([('id', 'in', partner_ids_id)])

            for partner in partner_ids:

                partner_name = partner.name
                if not partner.name:
                    if not partner.parent_id.name:
                        raise exceptions.ValidationError(_('Partner (#')+partner.id+_(') : Name is required to export.'))
                        return False
                    else:
                        partner_name = partner.parent_id.name

                partner_ref = partner.ref
                if not partner.ref:
                    if not partner.parent_id.ref:
                        raise exceptions.ValidationError(_('Partner (')+partner.name+_(') : Reference is required to export.'))
                        return False
                    else:
                        partner_ref = partner.parent_id.ref

                partner_fiscal_position = partner.property_account_position_id
                if not partner.property_account_position_id:
                    if not partner.parent_id.property_account_position_id:
                        raise exceptions.ValidationError(_('Partner (')+partner.name+_(') : Fiscal Position is required to export.'))
                        return False
                    else:
                        partner_fiscal_position = partner.parent_id.property_account_position_id

                if not partner_fiscal_position.sage_status:
                    raise exceptions.ValidationError(_('Fiscal Position (')+partner.property_account_position_id.name+_(') : Sage Status is required to export.'))
                    return False

                partner_vat = partner.vat
                if not partner.vat:
                    partner_vat = partner.parent_id.vat

                row = db.row()
                row.cid = self.removeSpecialChars(partner_ref)
                row.ccustype = partner_type['ccustype']
                row.csuptype = partner_type['csuptype']
                row.cname1 = self.removeSpecialChars(partner_name)
                row.caddress1 = self.removeSpecialChars(partner.street) if partner.street else ""
                row.caddress2 = self.removeSpecialChars(partner.street2) if partner.street2 else ""
                row.czipcode = partner.zip if partner.zip else ""
                row.clocality = self.removeSpecialChars(partner.city) if partner.city else ""
                row.ccountry = partner.country_id.code if partner.country_id else ""
                if partner_fiscal_position.sage_status == 'thirdcountry':
                    row.cvatref = "EX"
                else:
                    row.cvatref = partner.vat[:2] if partner.vat else ""
                row.cvatno = partner_vat[2:] if partner_vat else ""
                if partner_fiscal_position.sage_status == 'counterparty':
                    row.cvatcat = "X"
                elif not partner_vat:
                    row.cvatcat = "N"
                else:
                    row.cvatcat = " "
                row.clanguage = partner.lang[:2]
                row.cbankno = self.getBankNumberForPartner(partner)
                row.apply()
            db.close()

        # INVOICES

        for invoice_type in invoices_type_list:

            db = DbObject(join(tmpdir, invoice_type['db_header_name']), invoice_structure)
            db_line = DbObject(join(tmpdir, invoice_type['db_line_name']), invoice_line_structure)

            for invoice in self.invoice_ids:
                if invoice.type in invoice_type['types']:

                    if not invoice.number:
                        raise exceptions.ValidationError(_('Invoice (#')+invoice.id+_(') : Number is required to export.'))
                        return False

                    if re.sub("\D", "", invoice.number) == '':
                        raise exceptions.ValidationError(_('Invoice (')+invoice.number+_(') : Number must contain numeric value to export.'))
                        return False

                    if not invoice.date:
                        raise exceptions.ValidationError(_('Invoice (')+invoice.number+_(') : Date is required to export.'))
                        return False

                    if not invoice.date_due:
                        raise exceptions.ValidationError(_('Invoice (')+invoice.number+_(') : Due Date is required to export.'))
                        return False

                    if not invoice.amount_total:
                        raise exceptions.ValidationError(_('Invoice (')+invoice.number+_(') : Total Amount is required to export.'))
                        return False

                    partner_ref = invoice.partner_id.ref
                    if not invoice.partner_id.ref:
                        if not invoice.partner_id.parent_id.ref:
                            raise exceptions.ValidationError(_('Partner (')+invoice.partner_id.name+_(') : Reference is required to export.'))
                            return False
                        else:
                            partner_ref = invoice.partner_id.parent_id.ref

                    # if not invoice.reference:
                    #     raise exceptions.ValidationError(_('Invoice (')+invoice.number+_(') : Reference is required to export.'))
                    #     return False

                    # if re.sub("\D", "", invoice.reference) == '':
                    #     raise exceptions.ValidationError(_('Invoice (')+invoice.number_(+') : Reference must contain numeric value to export.'))
                    #     return False

                    # Set basic info for invoice
                    row = db.row()
                    row.tdbk = invoice_type['journal']
                    date = fields.Date.from_string(invoice.date)
                    row.tfyear = date.strftime("%Y")
                    row.tyear = date.year
                    row.tmonth = date.month
                    row.tdocno = int(re.sub("\D", "", invoice.number))
                    row.tdocdate = date
                    row.ttypcie = invoice_type['doc_type']
                    row.tcompan = self.removeSpecialChars(partner_ref)
                    row.tduedate = fields.Date.from_string(invoice.date_due)
                    row.tamount = invoice.amount_total
                    row.tremint = invoice.number
                    row.tremext = self.removeSpecialChars(invoice.reference) if invoice.reference else invoice.number
                    row.tintmode = "S"
                    row.tinvvcs = row.tremext #re.sub("\D", "", invoice.reference)
                    row.apply()

                    # Super check for 0,01€ of difference between the sum of vat lines and total sum (cfr question of rounding at DIFRA SA
                    # We will check if the sum of all base + vat of all lines is equal to the amount_total in the invoice
                    # If yes, ok let's do it
                    # If not and if the difference is exactly 0,01€, lets's add 0,01€ in the base of the first line, this will balance
                    check_total = 0
                    cents_to_add_in_base = False
                    for invoice_line in invoice.invoice_line_ids:
                        if invoice_line.invoice_line_tax_ids:
                            tax_line_with_sage_code = False
                            for line_tax in invoice_line.invoice_line_tax_ids:
                                if line_tax.sage_code:
                                    tax_line_with_sage_code = line_tax
                                    break
                            if not tax_line_with_sage_code:
                                raise exceptions.ValidationError(_('Tax (')+invoice_line.invoice_line_tax_ids[0].name+_(') : Sage Export Code is required to export.'))

                        taxes = invoice_line.get_taxes_values()
                        tax_count = 0
                        for tax in taxes:
                            tax_id = self.env['account.tax'].browse(taxes[tax]['tax_id'])
                            if tax_id == tax_line_with_sage_code or (len(tax_line_with_sage_code.children_tax_ids) > 0 and tax_id in tax_line_with_sage_code.children_tax_ids):
                                # Only add the base 1 time
                                if tax_count == 0:
                                    check_total += round(taxes[tax]['base'], invoice_line.currency_id.decimal_places)
                                    check_total += round(taxes[tax]['amount'], invoice_line.currency_id.decimal_places)
                                else:
                                    check_total += round(taxes[tax]['amount'], invoice_line.currency_id.decimal_places)

                                tax_count = tax_count + 1

                    check_total = round(check_total, invoice_line.currency_id.decimal_places)
                    if abs(check_total - invoice.amount_total) != 0:
                        cents_to_add_in_base = abs(check_total - invoice.amount_total)
                        if round(cents_to_add_in_base, invoice_line.currency_id.decimal_places) > 0.01:
                            raise exceptions.ValidationError(_('Error of ' + str(cents_to_add_in_base) + ' (> 0.01) in the total of the ' + invoice_type['journal'] + ' invoice: ' + str(invoice.number) + ', partner ' + str(invoice.partner_id.name)))
                    # End of the super check for 0,01€ error

                    # Add lines
                    line_count = 0
                    for invoice_line in invoice.invoice_line_ids:

                        if not invoice_line.account_id:
                            raise exceptions.ValidationError(_('Invoice Line (Invoice ')+invoice.number+_(') : Account is required to export.'))
                            return False

                        if not invoice_line.account_id.code:
                            raise exceptions.ValidationError(_('Account (')+invoice_line.account_id.name+_(') : Short Code is required to export.'))
                            return False

                        if invoice_line.invoice_line_tax_ids:
                            tax_line_with_sage_code = False
                            for line_tax in invoice_line.invoice_line_tax_ids:
                                if line_tax.sage_code:
                                    tax_line_with_sage_code = line_tax
                            if not tax_line_with_sage_code:
                                raise exceptions.ValidationError(_('Tax (')+invoice_line.invoice_line_tax_ids[0].name+_(') : Sage Export Code is required to export.'))

                        row_line = db_line.row()
                        row_line.tdbk = row.tdbk
                        row_line.tfyear = row.tfyear
                        row_line.tyear = row.tyear
                        row_line.tmonth = row.tmonth
                        row_line.tdocno = row.tdocno
                        row_line.tdocline = line_count
                        row_line.ttypeline = "S"
                        row_line.tdocdate = fields.Date.from_string(invoice_line.invoice_id.date)
                        row_line.tacttype = "A"
                        row_line.taccount = invoice_line.account_id.code
                        # Amounts
                        base = 0
                        vat = 0
                        taxes = invoice_line.get_taxes_values()
                        tax_count = 0
                        for tax in taxes:
                            tax_id = self.env['account.tax'].browse(taxes[tax]['tax_id'])
                            if tax_id == tax_line_with_sage_code or (len(tax_line_with_sage_code.children_tax_ids) > 0 and tax_id in tax_line_with_sage_code.children_tax_ids):
                                # Only add the base 1 time
                                if tax_count == 0:
                                    base += round(taxes[tax]['base'], invoice_line.currency_id.decimal_places)
                                    vat += round(taxes[tax]['amount'], invoice_line.currency_id.decimal_places)
                                else:
                                    vat += round(taxes[tax]['amount'], invoice_line.currency_id.decimal_places)

                                tax_count = tax_count + 1

                        # If error before remove the cents in the base at the first line
                        if line_count == 0:
                            base -= cents_to_add_in_base

                        row_line.tamount = base
                        row_line.tbasvat = base
                        row_line.tbaslstamn = base
                        
                        row_line.tvattotamn = vat
                        row_line.tvatamn = vat
                        row_line.tvatdblamn = 0
                        
                        row_line.tvstored = tax_line_with_sage_code.sage_code.code #invoice_line.invoice_line_tax_ids[0].sage_code.code if invoice_line.invoice_line_tax_ids else ""
                        row_line.tdc = invoice_type['line_doc_type_invoice' if invoice_line.price_subtotal_signed > 0 else 'line_doc_type_refund']
                        row_line.trem = self.removeSpecialChars(invoice.partner_id.name)
                        if self.analytic_plan != False:
                            if invoice_line.account_analytic_id != None:
                                if invoice_line.account_analytic_id:
                                    row_line.__setattr__(str(self.analytic_plan), invoice_line.account_analytic_id.sage_50_analytic_code)
                        row_line.apply()
                        line_count += 1

            db.close()
            db_line.close()

        ### ZIP AND SAVE ###
        temp = tempfile.mktemp(suffix='')
        shutil.make_archive(temp, 'zip', tmpdir)
        fn = open('%s.zip' % temp, 'rb')
        self.export_file = base64.encodestring(fn.read())
        fn.close()

        ### MARK INVOICES AS EXPORTED ###
        for invoice in self.invoice_ids:
            invoice.is_exported_to_sage_50 = True

        return True

    def removeSpecialChars(self, string):
        if not string:
            return string
        string = string.replace(str("ë"), "e")
        string = string.replace(str("Ë"), "E")
        string = string.replace(str("ö"), "oe")
        string = string.replace(str("Ö"), "OE")
        string = string.replace(str("ü"), "u")
        string = string.replace(str("Ü"), "u")
        string = string.replace(str("ä"), "ae")
        string = string.replace(str("Ä"), "AE")
        string = string.replace(str("ß"), "ss")
        string = string.replace(str("ß"), "ss")
        string = string.replace(str("é"), "e")
        string = string.replace(str("è"), "e")
        string = string.replace(str("ê"), "e")
        string = string.replace(str("ë"), "e")
        string = string.replace(str("î"), "i")
        string = string.replace(str("ï"), "i")
        string = string.replace(str("â"), "a")
        string = string.replace(str("à"), "a")
        string = string.replace(str("ù"), "u")
        string = string.replace(str("û"), "u")
        string = string.replace(str("ò"), "o")
        string = string.replace(str("ô"), "o")

        return string

    def getBankNumberForPartner(self, partner):
        if partner.parent_id:
            partner = partner.parent_id
        if partner.bank_account_count == 0:
            return ""
        first_bank_account = partner.bank_ids[0].acc_number
        first_bank_account = first_bank_account.replace("-", "")
        first_bank_account = first_bank_account.replace(".", "")
        first_bank_account = first_bank_account.replace(" ", "")

        return first_bank_account
            
class ExportFileCustom(models.Model):
    '''Export Sage 50 Wizard'''
    _name = 'export_sage_50.export_file_wizard'
    _description = 'Export File For Sage 50 Wizard'
    
    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")
    
    export_file_id = fields.Many2one('export_sage_50.export_file',string="Export File")
    
    @api.multi
    def action_export_custom(self):
        self.ensure_one()
        return self.export_file_id.action_export_custom(self.date_from, self.date_to)
