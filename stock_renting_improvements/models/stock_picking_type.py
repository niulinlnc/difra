# (c) AbAKUS IT Solutions
import logging
from odoo import models, fields, api, _

_logger = logging.getLogger(__name__)


class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    is_renting = fields.Boolean(default=False)
    renting_note = fields.Text(translate=True)
