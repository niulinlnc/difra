# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    life_date = fields.Datetime("End of Life Date", related='lot_id.life_date')
    tracking = fields.Selection(related='product_id.tracking')
