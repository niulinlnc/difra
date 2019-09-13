# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _ 

import logging
_logger = logging.getLogger(__name__)

class PricelistItem(models.Model):
    _inherit = 'product.pricelist.item'

    @api.multi
    def update_line(self):
        for line in self:
            # Get the base price for this product
            fix_price = line.product_tmpl_id.standard_price if (line.pricelist_id.price_origin == 'cost_price') else line.product_tmpl_id.list_price

            # Apply margin
            fix_price = fix_price * (1 + (line.pricelist_id.price_margin / 100))

            # Apply rounding
            fix_price = line.pricelist_id.get_price_rounded(fix_price, line.product_tmpl_id)[0]

            # Update line
            line.fixed_price = fix_price
            line.date_start = line.pricelist_id.date_valid_from
            line.date_end = line.pricelist_id.date_valid_to