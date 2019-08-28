# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class ProductSeqField(models.Model):
    _inherit = 'product.product'
    
    default_code = fields.Char("Internal Reference (seq*)", index=True, default=lambda self:self.env['ir.sequence'].get('product_sequenced_field'))
