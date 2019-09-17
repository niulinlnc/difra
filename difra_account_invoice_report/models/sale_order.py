# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
from datetime import datetime
import logging
_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def action_invoice_create(self, grouped=False, final=False):
        res = super(SaleOrder, self).action_invoice_create(grouped, final)
        for invoice in self.invoice_ids:
            for line in self.order_line:
                invoice_lines = invoice.invoice_line_ids.search([('product_id', '=', line.product_id.id)])
                for invoice_line in invoice_lines:
                    invoice_line_name = invoice_line.name
                    for move in line.move_ids:
                        if not move.has_been_invoiced:
                            move.write({'has_been_invoiced': True})
                            for move_line in move.move_line_ids:
                                prefix = "SN"
                                if move_line.product_id.tracking == 'lot':
                                    prefix = "Lot"
                                if move_line.lot_id:
                                    invoice_line_name = invoice_line_name + "\n%s: %s" % (prefix, move_line.lot_id.name)
                                elif move_line.lot_name:
                                    invoice_line_name = invoice_line_name + "\n%s: %s" % (prefix, move_line.lot_name)
                                if move_line.life_date:
                                    date = datetime.strptime(move_line.life_date, "%Y-%m-%d %H:%M:%S")
                                    invoice_line_name = invoice_line_name + "\n%s/%s/%s" % (date.day, date.month, date.year)
                    invoice_line.write({'name': invoice_line_name})
            if self.client_order_ref:
                invoice.write({'customer_order_reference': self.client_order_ref})
        return res
