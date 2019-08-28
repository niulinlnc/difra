# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _
from odoo.addons import decimal_precision as dp

import logging
_logger = logging.getLogger(__name__)

class ProductSupplierInfo(models.Model):
    _inherit = 'product.supplierinfo'

    # Existing Odoo Field
    price = fields.Float(string="Raw Purchase Price", help="Raw Purchase Price (in supplier currency)", default=0.0, digits=dp.get_precision('Product Price'), required=True)
    purchase_raw_price_company_currency = fields.Float(string="Raw Purchase Price", help="Raw Purchase Price (in curent company currency)", default=0.0, digits=dp.get_precision('Product Price'), compute='_compute_purchase_net_price')

    purchase_discount = fields.Float(string="Purchase discount (%)")
    purchase_net_price = fields.Float(string="Purchase net price", compute='_compute_purchase_net_price', digits=dp.get_precision('Product Price'))
    purchase_net_price_company_currency = fields.Float(string="Net Purchase Price", help="Net Purchase Price (in curent company currency)", default=0.0, digits=dp.get_precision('Product Price'), compute='_compute_purchase_net_price')

    supplier_sale_price_method = fields.Selection([('net', 'On net price'), ('raw', 'On raw price')], string="Sale price method", default='raw')
    supplier_sale_default_discount = fields.Float(string="Sale default margin (%)")
    sale_net_price = fields.Float(string="Sale price", compute='_compute_purchase_net_price', digits=dp.get_precision('Product Price'))
    inherit_price_info_from_supplier = fields.Boolean(string="Inherit from Supplier", default=True)

    company_currency_id = fields.Many2one(related='company_id.currency_id', string="Company Currency", readonly=True, store=True)

    @api.onchange('name', 'inherit_price_info_from_supplier')
    def _set_default_values_discount(self):
        if self.inherit_price_info_from_supplier:
            if self.name == None:
                self.purchase_discount = 0
            self.purchase_discount = self.name.purchase_discount
            self.supplier_sale_price_method = self.name.supplier_sale_price_method
            self.supplier_sale_default_discount = self.name.supplier_sale_default_discount

    @api.multi
    @api.onchange('price', 'currency_id', 'purchase_discount', 'supplier_sale_price_method', 'supplier_sale_default_discount')
    def _compute_purchase_net_price(self):
        for productinfo in self:
            # Purchase raw price in current company currency
            productinfo.purchase_raw_price_company_currency = productinfo.currency_id.compute(productinfo.price, productinfo.company_currency_id, False)
            # Purchase net price
            productinfo.purchase_net_price = productinfo.price - (productinfo.price * productinfo.purchase_discount / 100)
            # Purchase net price in current company currency
            productinfo.purchase_net_price_company_currency = productinfo.currency_id.compute(productinfo.purchase_net_price, productinfo.company_currency_id, False)

            # Sale
            if productinfo.supplier_sale_price_method == 'net':
                productinfo.sale_net_price = productinfo.purchase_net_price_company_currency + (productinfo.purchase_net_price_company_currency * productinfo.supplier_sale_default_discount / 100)
            elif productinfo.supplier_sale_price_method == 'raw':
                productinfo.sale_net_price = productinfo.purchase_raw_price_company_currency + (productinfo.purchase_raw_price_company_currency * productinfo.supplier_sale_default_discount / 100)

            productinfo.product_tmpl_id.compute_purchase_and_sale_price()
