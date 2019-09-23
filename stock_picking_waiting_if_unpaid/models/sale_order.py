# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
import logging

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    payment_before_delivery = fields.Boolean(related="payment_term_id.payment_before_delivery")

    @api.multi
    @api.onchange('sale.order.lines')
    def action_force_invoice(self):
        for so in self:
            if so.payment_term_id and so.payment_term_id.payment_before_delivery:
                for line in so.order_line:
                    if line.qty_to_invoice == 0:
                        line.write({'qty_to_invoice': line.product_uom_qty - line.qty_invoiced})
