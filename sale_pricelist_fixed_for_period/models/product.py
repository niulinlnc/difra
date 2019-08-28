# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, tools, _
from odoo.addons import decimal_precision as dp

import logging
_logger = logging.getLogger(__name__)

class Product(models.Model):
    _inherit = 'product.template'

    @api.multi
    def _compute_pricelist_count(self):
        for product in self:
            product.pricelist_count = self.env['product.pricelist'].search_count([('item_ids.product_tmpl_id', '=', product.id)])

    pricelist_count = fields.Integer(string="Pricelist count", compute=_compute_pricelist_count)
            