# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
import logging
_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    products_delivered = fields.Boolean("Products Delivered", default=False, compute='_compute_products_delivered')

    @api.one
    def _compute_products_delivered(self):
        self.ensure_one()
        # product_uom_qty = 0
        # product_delivered_qty = 0
        # for line in self.order_line:
        #     product_uom_qty += line.product_uom_qty
        #     product_delivered_qty += line.qty_delivered
        # self.products_delivered = product_delivered_qty >= product_uom_qty

        picks_state = self.picking_ids.mapped('state')
        nb_active = 0
        nb_cancel = 0
        for pick_state in picks_state:
            if pick_state not in ['done', 'cancel']:
                nb_active += 1
            elif pick_state == 'cancel':
                nb_cancel += 1
        if len(self.picking_ids) > 0 and nb_cancel < len(self.picking_ids) and nb_active == 0:
            self.products_delivered = True
        else:
            self.products_delivered = False
