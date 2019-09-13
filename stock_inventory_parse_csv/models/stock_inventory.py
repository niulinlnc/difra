# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
import logging
_logger = logging.getLogger(__name__)


class StockInventory(models.Model):
    _inherit = 'stock.inventory'

    csv_inventory = fields.Text(string="CSV Inventory")

    @api.one
    def action_parse_csv(self):
        if self.csv_inventory:
            text = ""
            for line in self.csv_inventory.split('\n'):
                if line:
                    line_tab = line.split(';')
                    ref = line_tab[0]
                    qty = line_tab[1]
                    template = self.env['product.template'].search([('default_code', '=', ref)])
                    product = self.env['product.product'].search([('default_code', '=', template.default_code)])
                    if len(template) > 1:
                        text += ref + ";" + qty + ";=> More than 1 result for this reference\n"
                    elif len(template) == 0:
                        if len(self.env['product.template'].search([('default_code', '=', ref), ('active', '=', False)])) > 0:
                            text += ref + ";" + qty + ";=>Product archived"
                        elif len(product == 0):
                            text += ref + ";" + qty + ";=> Not found\n"
                        else:
                            text += ref + ";" + qty + ";=>Wrong Reference\n"
                    elif len(product) == 0:
                        text += ref + ";" + qty + ";=>No Variant\n"
                    elif len(product) == 1 and product.default_code != template.default_code:
                        text += ref + ";" + qty + ";=>Wrong Reference\n"
                    else:
                        if template.tracking != 'none':
                            text += ref + ";" + qty + ";=> Serial/Lot Number required\n"
                        elif template.type != "product":
                            text += ref + ";" + qty + ";=> Product type is not stockable\n"
                        else:
                            line_found = self.line_ids.search([('product_id.id', '=', template.id), ('inventory_id.id', '=', self.id)])
                            if not line_found:
                                vals = {
                                    'product_id': template.id,
                                    'product_qty': qty,
                                    'inventory_id': self.id,
                                    'location_id': self.location_id.id
                                }
                                result = self.write({'line_ids': [(0, _, vals)]})
                            else:
                                line_found.product_qty = qty
            self.csv_inventory = text
