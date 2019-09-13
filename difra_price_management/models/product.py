# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    margin_raw = fields.Float(string="Raw margin", compute='_compute_margin')
    margin_abs = fields.Char(string="Abs margin", compute='_compute_margin')

    @api.multi
    @api.onchange('seller_ids')
    def compute_purchase_and_sale_price(self):
        for product in self:
            if product.purchase_ok == True and len(product.seller_ids) > 0:
                #_logger.debug("\n\n COMPUTE STANDARD AND LIST PRICE FROM SELLERS: %s - %s - %s\n\n\n", product.purchase_ok, product.id, product.name)
                sellerinfo = product.seller_ids.sorted(key=lambda r: r.sequence)[0]
                product.standard_price = sellerinfo.purchase_net_price_company_currency
                product.list_price = sellerinfo.sale_net_price

    @api.onchange('standard_price', 'list_price')
    def _compute_margin(self):
        for product in self:
            product.margin_raw = product.list_price - product.standard_price
            if product.standard_price != 0:
                margin_abs = ((product.list_price / product.standard_price) * 100)
                product.margin_abs = ("%.4f %%" % round(margin_abs, 4))
            else:
                product.margin_abs = "0 %"

    @api.depends('product_variant_ids', 'product_variant_ids.standard_price')
    def _compute_standard_price(self):
        for product in self:
            if product.purchase_ok == True and len(product.seller_ids) > 0:
                #_logger.debug("\n\n COMPUTE STANDARD PRICE FROM SELLERS: %s\n\n\n", product.purchase_ok)
                sellerinfo = product.seller_ids.sorted(key=lambda r: r.sequence)[0]
                product.standard_price = sellerinfo.purchase_net_price_company_currency
            else:
                super(ProductTemplate, self)._compute_standard_price()
