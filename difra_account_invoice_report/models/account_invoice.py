# -*- coding: utf-8 -*-
from . import account_tax

from odoo import models, fields, api, exceptions, _
import logging
_logger = logging.getLogger(__name__)


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    delivery_order_ids = fields.Many2many('stock.picking', string="Linked Delivery Orders", compute="_compute_delivery_orders")

    @api.multi
    def _compute_delivery_orders(self):
        for invoice in self:
            picking_ids = self.env['stock.picking']
            for line in invoice.invoice_line_ids:
                for sol in line.sale_line_ids:
                    for move in sol.move_ids:
                        if move.picking_id and move.picking_id.picking_type_id == self.env.ref('stock.picking_type_out') and move.picking_id.state != 'cancel':
                            if move.picking_id not in picking_ids:
                                picking_ids |= move.picking_id
            invoice.delivery_order_ids = picking_ids
