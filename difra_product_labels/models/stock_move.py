# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models


class StockMove(models.Model):
    _inherit = 'stock.move'

    @api.multi
    def print_line_labels(self):
        if self.picking_id.picking_type_id.code == 'incoming':
            return self.env.ref('difra_product_labels.difra_move_complete_label_internal_report').report_action(self)
        if self.picking_type_id.code == 'outgoing':
            return self.env.ref('difra_product_labels.difra_move_complete_label_external_report').report_action(self)

    @api.multi
    def print_line_single_label(self):
        if self.picking_id.picking_type_id.code == 'incoming':
            return self.env.ref('difra_product_labels.difra_move_single_label_internal_report').report_action(self)
        if self.picking_type_id.code == 'outgoing':
            return self.env.ref('difra_product_labels.difra_move_single_label_external_report').report_action(self)
        
