# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    move_line_ids = fields.One2many('stock.move.line', compute="_compute_move_line_ids")
    partner_id = fields.Many2one('res.partner', compute="_compute_partner_id")

    @api.depends('move_line_ids', 'location_id')
    def _compute_partner_id(self):
        for quant in self:
            move = quant.move_line_ids.sorted(key=lambda r: r.date)[0]
            if move and quant.location_id == move.location_dest_id:
                quant.partner_id = move.partner_id.id


    @api.depends('product_id', 'location_id', 'lot_id', 'package_id')
    def _compute_move_line_ids(self):
        for quant in self:
            quant.move_line_ids = self.env['stock.move.line'].search([
                ('product_id', '=', quant.product_id.id),
                '|',
                    ('location_id', '=', quant.location_id.id),
                    ('location_dest_id', '=', quant.location_id.id),
                ('lot_id', '=', quant.lot_id.id),
                '|',
                    ('package_id', '=', quant.package_id.id),
                    ('result_package_id', '=', quant.package_id.id),
                ('state', '=', 'done')
            ])
