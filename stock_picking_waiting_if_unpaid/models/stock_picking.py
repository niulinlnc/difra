# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
import logging

_logger = logging.getLogger(__name__)


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.depends('move_type', 'move_lines.state', 'move_lines.picking_id')
    @api.one
    def _compute_state(self):
        super(StockPicking, self)._compute_state()
        if self.state == "assigned" \
                and self.sale_id \
                and self.sale_id.payment_term_id.payment_before_delivery \
                and (self.sale_id.invoice_ids
                     and not all(i.state in ["paid", "cancel"] for i in self.sale_id.invoice_ids)
                     or not self.sale_id.invoice_ids):
            self.state = 'confirmed'
