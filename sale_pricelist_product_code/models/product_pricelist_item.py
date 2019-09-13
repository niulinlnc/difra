# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _
from odoo.addons import decimal_precision as dp

import logging
_logger = logging.getLogger(__name__)

class PricelistItem(models.Model):
    _inherit = 'product.pricelist.item'

    product_reference = fields.Char(compute='_compute_product_reference', string="Reference")

    @api.one
    @api.depends('applied_on', 'product_tmpl_id', 'product_id')
    def _compute_product_reference(self):
        if self.applied_on == '0_product_variant':
            self.product_reference = self.product_id.default_code
        elif self.applied_on == '1_product':
            self.product_reference = self.product_tmpl_id.default_code
        else:
            self.product_reference = "/"