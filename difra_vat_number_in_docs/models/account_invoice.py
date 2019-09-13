# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    partner_vat = fields.Char(related='partner_id.vat', string="VAT")
    