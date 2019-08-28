# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _
from odoo.addons import decimal_precision as dp

import logging
_logger = logging.getLogger(__name__)

class PricelistItem(models.Model):
    _inherit = 'product.pricelist.item'

    product_computed_price = fields.Float(compute='_compute_product_price', string="Price", digits=dp.get_precision('Product Price'))

    @api.one
    @api.depends('applied_on', 'compute_price', 'base', 'product_tmpl_id', 'fixed_price', 'base_pricelist_id', 'percent_price', 'price_discount', 'price_max_margin', 'price_min_margin', 'price_round', 'product_id', 'price_surcharge')
    def _compute_product_price(self):
        price = 0.0
        if self.applied_on == '0_product_variant':
            product = self.product_id.with_context(
                lang=self.env.user.partner_id.lang,
                quantity=self.min_quantity,
                pricelist=self.pricelist_id.id,
                uom=self.product_id.uom_id.id
            )
            price = product['price']
        elif self.applied_on == '1_product':
            product = self.product_tmpl_id.with_context(
                lang=self.env.user.partner_id.lang,
                quantity=self.min_quantity,
                pricelist=self.pricelist_id.id,
                uom=self.product_id.uom_id.id
            )
            price = product['price']
        self.product_computed_price = price
        return price
