# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    cost_history_count = fields.Integer(string="Cost History Count", compute='_compute_cost_history_count')

    @api.one
    def _compute_cost_history_count(self):
        self.cost_history_count = len(self.env['product.cost.history'].search([('product_id.product_tmpl_id.id', '=', self.id)]))