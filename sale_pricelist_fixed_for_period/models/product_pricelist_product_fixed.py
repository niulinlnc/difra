# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, tools, _
from odoo.addons import decimal_precision as dp

import logging
_logger = logging.getLogger(__name__)

class PricelistProductFixed(models.Model):
    _name = 'product.pricelist.product.fixed'
    _order = 'default_code asc, product_id asc'

    pricelist_id = fields.Many2one('product.pricelist', string="Pricelist", ondelete='cascade')
    product_id = fields.Many2one('product.template', string="Product")
    default_code = fields.Char(related='product_id.default_code', string="Internal Reference", readonly=True)
    currency_id = fields.Many2one('res.currency', default=lambda self: self.pricelist_id.currency_id)
    cost_price = fields.Float(related='product_id.standard_price', string="Cost price", readonly=True)
    sale_price = fields.Float(related='product_id.list_price', string="Sale price", readonly=True)
    price_origin = fields.Selection([('cost_price', 'Cost Price'), ('sale_price', 'Sale Price')], string="Based on", default='cost_price', required=True)
    price_margin = fields.Float(string="Applied margin (%)", default=0, required=True)

    # The 4 following fields are exact copy of what Odoo does in the PL-item basis, we will apply the same method
    price_round = fields.Float(
        'Price Rounding', digits=dp.get_precision('Product Price'),
        help="Sets the price so that it is a multiple of this value.\n"
             "Rounding is applied after the discount and before the surcharge.\n"
             "To have prices that end in 9.99, set rounding 10, surcharge -0.01")
    price_min_margin = fields.Float(
        'Min. Price Margin', digits=dp.get_precision('Product Price'),
        help='Specify the minimum amount of margin over the base price.')
    price_max_margin = fields.Float(
        'Max. Price Margin', digits=dp.get_precision('Product Price'),
        help='Specify the maximum amount of margin over the base price.')
    price_surcharge = fields.Float(
        'Price Surcharge', digits=dp.get_precision('Product Price'),
        help='Specify the fixed amount to add or substract(if negative) to the amount calculated with the discount.')

    @api.one
    def get_price_rounded(self, price, product):
        price_limit = price
        qty_uom_id = self._context.get('uom') or product.uom_id.id
        price_uom = self.env['product.uom'].browse([qty_uom_id])
        convert_to_price_uom = (lambda price: product.uom_id._compute_price(price, price_uom))
        
        # Rounding
        if self.price_round:
            price = tools.float_round(price, precision_rounding=self.price_round)

        # Surcharge
        if self.price_surcharge:
            price_surcharge = convert_to_price_uom(self.price_surcharge)
            price += price_surcharge

        # Min margin
        if self.price_min_margin:
            price_min_margin = convert_to_price_uom(self.price_min_margin)
            price = max(price, price_limit + price_min_margin)

        # Max margin
        if self.price_max_margin:
            price_max_margin = convert_to_price_uom(self.price_max_margin)
            price = min(price, price_limit + price_max_margin)
        
        return price
