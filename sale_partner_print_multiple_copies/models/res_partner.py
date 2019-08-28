# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class PartnerWithCopyNumbers(models.Model):
    _inherit = 'res.partner'

    sale_order_copy_number = fields.Integer('Number of copies for SO', default=1)
    purchase_order_copy_number = fields.Integer('Number of copies for PO', default=1)
    invoice_copy_number = fields.Integer('Number of copies for Invoice', default=1)