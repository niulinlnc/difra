# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
from odoo import models, fields, api, exceptions, _


class MRPBOMLine(models.Model):
    _inherit = 'mrp.bom.line'

    product_checked = fields.Boolean(related='product_id.checked')