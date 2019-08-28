# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _ 

import logging
_logger = logging.getLogger(__name__)

class PricelistItem(models.Model):
    _inherit = 'product.pricelist.item'

    # Just redefined to change the string of "Public Price" to "Sale Price"
    base = fields.Selection([
        ('list_price', 'Sale Price'),
        ('standard_price', 'Cost Price'),
        ('pricelist', 'Other Pricelist')], "Based on",
        default='list_price', required=True,
        help='Base price for computation.\n'
             'Public Price: The base price will be the Sale/public Price.\n'
             'Cost Price : The base price will be the cost price.\n'
             'Other Pricelist : Computation of the base price based on another Pricelist.')

    margin_discount_operation = fields.Selection([
        ('plus', '+'),
        ('minus', '-'),], default='plus')

    @api.one
    @api.depends('categ_id', 'product_tmpl_id', 'product_id', 'compute_price', 'fixed_price', \
        'pricelist_id', 'percent_price', 'price_discount', 'price_surcharge')
    def _get_pricelist_item_name_price(self):
        if self.categ_id:
            self.name = _("Category: %s") % (self.categ_id.name)
        elif self.product_tmpl_id:
            self.name = self.product_tmpl_id.name
        elif self.product_id:
            self.name = self.product_id.display_name.replace('[%s]' % self.product_id.code, '')
        else:
            self.name = _("All Products")

        if self.compute_price == 'fixed':
            self.price = ("%s %s") % (self.fixed_price, self.pricelist_id.currency_id.name)
        elif self.compute_price == 'percentage':
            self.price = _("%s %% discount") % (self.percent_price)
        else:
            if self.margin_discount_operation == 'plus':
                self.price = _("%s %% margin (+) and %s surcharge") % (abs(self.price_discount), self.price_surcharge)
            elif self.margin_discount_operation == 'minus':
                self.price = _("%s %% discount (-) and %s surcharge") % (abs(self.price_discount), self.price_surcharge)

    @api.onchange('compute_price')
    def _onchange_compute_price(self):
        if self.compute_price != 'fixed':
            self.fixed_price = 0.0
        if self.compute_price != 'percentage':
            self.percent_price = 0.0
        if self.compute_price != 'formula':
            self.update({
                'price_discount': 0.0,
                'price_surcharge': 0.0,
                'price_round': 0.0,
                'price_min_margin': 0.0,
                'price_max_margin': 0.0,
            })
