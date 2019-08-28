# (c) AbAKUS IT Solutions
import logging
from odoo import models, fields, api, _
_logger = logging.getLogger(__name__)


class StockLocationPath(models.Model):
    _inherit = 'stock.location.path'

    def _prepare_move_copy_values(self, move_to_copy, new_date):
        # Doesn't work, problem with second renting out.
        new_move_vals = super(StockLocationPath, self)._prepare_move_copy_values(move_to_copy, new_date)
        new_move_vals['partner_id'] = move_to_copy.picking_id.partner_id.id
        return new_move_vals
