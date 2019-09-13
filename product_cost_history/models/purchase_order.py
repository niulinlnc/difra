# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.multi
    def button_confirm(self):

        order_ids = []

        for order in self:
            if order.state in ['draft', 'sent']:
                order_ids.append(order.id)

        vals = super(PurchaseOrder, self).button_confirm()

        for order in self:
            if order.id in order_ids and order.state in ['purchase']:
                for line in order.order_line:
                    cost_id = self.env['product.cost.history'].search([('product_id', '=', line.product_id.id)], order="create_date desc", limit=1)

                    if not cost_id or cost_id.cost != line.price_unit:
                        self.env['product.cost.history'].create({
                            'product_id': line.product_id.id,
                            'cost': line.price_unit
                        })

        return vals