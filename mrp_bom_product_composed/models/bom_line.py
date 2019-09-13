# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions

from odoo import models, fields, api

class BOMLine(models.Model):
    _inherit = 'mrp.bom.line'
    
    product_contains_bom = fields.Boolean(string="BoM", compute="_compute_product_contains_bom")

    @api.multi
    @api.onchange('product_id')
    def _compute_product_contains_bom(self):
        for line in self:
            line.product_contains_bom = False
            if line.product_id.bom_count > 0:
                line.product_contains_bom = True