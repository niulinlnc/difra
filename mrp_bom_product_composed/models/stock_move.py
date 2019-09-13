# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class StockMove(models.Model):
    _inherit = 'stock.move'

    product_contains_bom= fields.Boolean(string="BoM", compute="_compute_product_contains_bom")

    @api.multi
    def _compute_product_contains_bom(self):
        for line in self:
            line.product_contains_bom = False
            if line.product_id.bom_count > 0:
                line.product_contains_bom = True
