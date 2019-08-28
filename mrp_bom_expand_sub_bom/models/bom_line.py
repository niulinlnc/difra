# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions

from odoo import models, fields, api

class BOMLine(models.Model):
    _inherit = 'mrp.bom.line'
    
    product_contains_bom = fields.Boolean(string="BoM", compute="_compute_product_contains_bom")

    @api.multi
    def expand_bom(self):
        for line in self:
            if line.product_contains_bom:
                # Get first BOM for product in current line
                first_product_bom = line.product_id.bom_ids[0]
                # For each line of this BOM, create a new line in the current BOM
                for sub_line in first_product_bom.bom_line_ids:
                    new_line = self.env['mrp.bom.line'].create({
                        'bom_id': line.bom_id.id,
                        'product_id': sub_line.product_id.id,
                        'product_qty': sub_line.product_qty,
                        'product_uom_id': sub_line.product_uom_id.id,
                        
                    })
                # Delete the current line
                line.unlink()