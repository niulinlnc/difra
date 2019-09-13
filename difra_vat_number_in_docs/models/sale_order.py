# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    partner_vat = fields.Char(related='partner_invoice_id.vat', string="VAT")
    