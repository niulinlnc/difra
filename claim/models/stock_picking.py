# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    origin_claim = fields.Many2one('claim', string="Source Claim")
    repair_id = fields.Many2one('mrp.repair')
    delivery_address = fields.Many2one('res.partner', related='repair_id.delivery_address')
