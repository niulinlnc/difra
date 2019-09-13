# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _

import logging

_logger = logging.getLogger(__name__)


class MarketFeedback(models.Model):
    _name = 'product.market_feedback'
    _inherit = ['mail.thread']

    description = fields.Text(string="Description", required=True)
    category_id = fields.Many2one('product.category')
    product_id = fields.Many2one('product.template', string="Product")

    @api.multi
    def name_get(self):
        result = []
        for feedback in self:
            result.append(
                (feedback.id, _("Market Feedback for %s (%s)") % (feedback.product_id.name, feedback.create_date)))
        return result
