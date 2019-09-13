# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
import logging
_logger = logging.getLogger(__name__)


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    origin_claim = fields.Many2one('claim', string="Source Claim")
    repair_id = fields.Many2one('mrp.repair')
    delivery_address = fields.Many2one('res.partner', related='repair_id.delivery_address')
    customer_reference = fields.Char(related="repair_id.customer_reference", string="Customer Order Reference")
    description = fields.Text(related='repair_id.description')
    product_repaired = fields.Many2one('product.product', related='repair_id.product_id', string="Product to repair")
    lot_id = fields.Many2one('stock.production.lot', related='repair_id.lot_id', string="Lot Repaired")
