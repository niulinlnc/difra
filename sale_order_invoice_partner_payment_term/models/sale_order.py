# -*- coding: utf-8 -*-
import logging
from odoo import models, fields, api, exceptions, _

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    @api.onchange('partner_invoice_id')
    def set_payment_term(self):
        for order in self:
            order.payment_term_id = order.partner_invoice_id.property_payment_term_id if order.partner_invoice_id.property_payment_term_id else False