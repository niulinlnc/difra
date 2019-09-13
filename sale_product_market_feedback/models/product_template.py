# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    market_feedback_ids = fields.One2many('product.market_feedback', 'product_id', groups="sales_team.group_sale_salesman")
    market_feedback_ids_qty = fields.Integer(compute="_compute_qty_market_feedbacks", string="Market Feedbacks", groups="sales_team.group_sale_salesman")

    @api.multi
    def _compute_qty_market_feedbacks(self):
        for template in self:
            template.market_feedback_ids_qty = len(self.env['product.market_feedback'].search(['|', ('product_id.id', '=', template.id), ('category_id.id', '=', template.categ_id.id)]))
