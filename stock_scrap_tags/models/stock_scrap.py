# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class StockScrap(models.Model):
    _inherit = 'stock.scrap'

    tag_id = fields.Many2one('stock.scrap.tag', string="Tag", required=True)
    note = fields.Text()
    standard_price = fields.Float(string="Cost", required=True, compute='_compute_price')

    @api.onchange('product_id')
    def _compute_price(self):
        for record in self:
            if record.product_id:
                record.standard_price = record.product_id.standard_price
