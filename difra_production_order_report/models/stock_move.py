# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
import logging
_logger = logging.getLogger(__name__)


class StockMove(models.Model):
    _inherit = 'stock.move'
    _order = 'usual_stock_location_info'

    usual_stock_location_info = fields.Char(related='product_id.usual_stock_location_info', string="Usual Stock Location", store=True)
