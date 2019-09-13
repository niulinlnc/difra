# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, tools, _
from odoo.addons import decimal_precision as dp

import logging
_logger = logging.getLogger(__name__)

class Pricelist(models.Model):
    _inherit = 'product.pricelist'

    pricelist_type = fields.Selection([('normal', 'Normal'), ('fixed_for_period', 'Fixed for a period on products')], string="Type", default='normal', required=True)
    help_text = fields.Text(default='This selections allow you to create temporary pricelists with fixed price for given products using prices computed on cost/sale price and margin')

    product_fixed_ids = fields.One2many('product.pricelist.product.fixed', 'pricelist_id', string="Selection of products", copy=True)
    date_valid_from = fields.Date(string="Valid from")
    date_valid_to = fields.Date(string="Valid to")

    @api.multi
    @api.depends('product_fixed_ids')
    def _compute_len_fixed_products(self):
        for pl in self:
            pl.product_ids_count = len(pl.product_fixed_ids)

    product_ids_count = fields.Integer(string="Products count", compute=_compute_len_fixed_products, store=True)

    @api.multi
    @api.depends('item_ids')
    def _compute_len_items(self):
        for pl in self:
            pl.item_ids_count = len(pl.item_ids)

    item_ids_count = fields.Integer(string="Lines count", compute=_compute_len_items, store=True)

    @api.multi
    def compute_lines(self):
        for pl in self:
            for product_setting in pl.product_fixed_ids:
                # Search if product exist in items list, if exist, we leave it as is
                line = self.env['product.pricelist.item'].search_count([('pricelist_id', '=', pl.id), ('product_tmpl_id', '=', product_setting.product_id.id)])
                if line == 0:
                    # Get the base price for this product
                    fix_price = product_setting.cost_price if (product_setting.price_origin == 'cost_price') else product_setting.sale_price

                    # Apply margin
                    fix_price = fix_price * (1 + (product_setting.price_margin / 100))

                    # Apply rounding
                    fix_price = product_setting.get_price_rounded(fix_price, product_setting.product_id)[0]

                    # Create one line with fixed price for this product
                    pricelist_item = self.env['product.pricelist.item'].create({
                        'pricelist_id': pl.id,
                        'applied_on': '1_product',
                        'product_tmpl_id': product_setting.product_id.id,
                        'date_start': pl.date_valid_from,
                        'date_end': pl.date_valid_to,
                        'compute_price': 'fixed',
                        'fixed_price': fix_price,
                    })

    @api.multi
    def update_lines(self):
        for pl in self:
            for product_setting in pl.product_fixed_ids:
                # Search if product exist in items list, if exist, we leave it as is
                line = self.env['product.pricelist.item'].search([('pricelist_id', '=', pl.id), ('product_tmpl_id', '=', product_setting.product_id.id)])
                if line:
                    # Get the base price for this product
                    fix_price = product_setting.cost_price if (product_setting.price_origin == 'cost_price') else product_setting.sale_price

                    # Apply margin
                    fix_price = fix_price * (1 + (product_setting.price_margin / 100))

                    # Apply rounding
                    fix_price = product_setting.get_price_rounded(fix_price, product_setting.product_id)[0]
                    
                    # Update the line
                    line.fixed_price = fix_price
                    line.date_start = line.pricelist_id.date_valid_from
                    line.date_end = line.pricelist_id.date_valid_to

    @api.multi
    def reset_lines(self):
        for pl in self:
            pl.item_ids.unlink()

    
    
                
                