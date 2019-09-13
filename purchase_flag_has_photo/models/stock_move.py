# (c) AbAKUS IT Solutions
import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class StockMove(models.Model):
    _inherit = "stock.move"

    has_photo = fields.Boolean(default=False)
