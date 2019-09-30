# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    partner_source_id = fields.Many2one('res.partner', string="Partner Source")