# -*- coding: utf-8 -*-
""" Extend sale.order.line to include a flag marking product to feature in print report
"""
from odoo import models, fields, api, exceptions, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    join_product_report = fields.Boolean(default=False)
