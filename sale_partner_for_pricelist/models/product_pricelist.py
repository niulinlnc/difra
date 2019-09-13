# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)


class ProductPricelist(models.Model):
    _inherit = 'product.pricelist'

    partner_ids = fields.One2many('res.partner', 'property_product_pricelist')
    partner_ids_count = fields.Integer(compute="_compute_partner_ids_count", string="Partners linked")
    
    @api.multi
    def _compute_partner_ids_count(self):
        for pl in self:
            # len(pl.partner_ids) #
            pl_id = 'product.pricelist,' + str(pl.id)
            pl.partner_ids_count = self.env['ir.property'].search_count([('name', '=', 'property_product_pricelist'), ('type', '=', 'many2one'), ('value_reference', '=', pl_id)])
            #partners = self.env['res.partner'].search([('property_product_pricelist', '=', pl.id)])
            #_logger.debug("\n\n Parters : %s", partners)
        