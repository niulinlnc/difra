# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    partner_source = fields.Many2one('res.partner', string="Partner source")