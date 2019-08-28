# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

class PickingList(models.Model):
    _inherit = 'stock.picking'

    partner_vat = fields.Char(related='partner_id.vat', string="VAT")
    