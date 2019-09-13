# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

import datetime
import logging
_logger = logging.getLogger(__name__)

class Partner(models.Model):
    _inherit = 'res.partner'

    purchase_discount = fields.Float(string="Purchase discount (%)")
    supplier_sale_price_method = fields.Selection([('net', 'On net price'), ('raw', 'On raw price')], string="Sale price method", default='raw')
    supplier_sale_default_discount = fields.Float(string="Sale default margin (%)")
    last_update = fields.Date(string='Last Update')

    @api.onchange('purchase_discount', 'supplier_sale_price_method', 'supplier_sale_default_discount')
    def _update_last_update(self):
        self.last_update = datetime.datetime.now()
    
    @api.multi
    def update_supplied_products(self):
        for partner in self:
            supplierinfo_ids = self.env['product.supplierinfo'].search([('name', '=', partner.id)])
            for info in supplierinfo_ids:
                if info.inherit_price_info_from_supplier:
                    info.write({
                        'purchase_discount': partner.purchase_discount,
                        'supplier_sale_price_method': partner.supplier_sale_price_method,
                        'supplier_sale_default_discount': partner.supplier_sale_default_discount,
                    })
                    info.product_tmpl_id.compute_purchase_and_sale_price()
            partner.last_update = datetime.datetime.now()
    