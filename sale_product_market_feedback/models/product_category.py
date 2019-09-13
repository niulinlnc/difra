# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)


class ProductCategory(models.Model):
    _inherit = 'product.category'

    market_feedback_ids = fields.One2many('product.market_feedback', 'category_id')
    market_feedback_ids_qty = fields.Integer(compute="_compute_qty_market_feedbacks", string="Market Feedbacks")

    @api.multi
    def _compute_qty_market_feedbacks(self):
        for cat in self:
            cat.market_feedback_ids_qty = len(cat.market_feedback_ids)