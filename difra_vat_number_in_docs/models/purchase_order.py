# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    partner_vat = fields.Char(related='partner_id.vat', string="VAT")
    