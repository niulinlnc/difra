# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
import logging
_logger = logging.getLogger(__name__)


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    repair_id = fields.Many2one('mrp.repair')
    customer_order_reference = fields.Char(related='repair_id.customer_reference', string="Customer Order Reference")
    description = fields.Text(related='repair_id.description', string="Description")
    product_id = fields.Many2one('product.product', related='repair_id.product_id', string="Product Repaired")
