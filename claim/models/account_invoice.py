# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
import logging
_logger = logging.getLogger(__name__)


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    customer_order_reference = fields.Char('Customer Order Reference')
    description = fields.Text("Description")
    product_id = fields.Many2one('product.template', string="Product Repaired")
