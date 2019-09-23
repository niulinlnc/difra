# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
import logging

_logger = logging.getLogger(__name__)


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.depends('state', 'product_uom_qty', 'qty_delivered', 'qty_to_invoice', 'qty_invoiced')
    def _compute_invoice_status(self):
        super(SaleOrderLine, self)._compute_invoice_status()
        for line in self:
            if line.order_id.payment_term_id and line.order_id.payment_term_id.payment_before_delivery:
                if line.qty_to_invoice == -1 and line.product_uom_qty == line.qty_invoiced:
                    line.write({'qty_to_invoice': 0, 'invoice_status': 'invoiced'})
