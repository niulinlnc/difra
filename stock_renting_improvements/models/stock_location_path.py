# (c) AbAKUS IT Solutions
import logging
from odoo import models, fields, api, _
_logger = logging.getLogger(__name__)


class StockLocationPath(models.Model):
    _inherit = 'stock.location.path'

    def _prepare_move_copy_values(self, move_to_copy, new_date):
        new_move_vals = {
            'origin': move_to_copy.origin or move_to_copy.picking_id.name or "/",
            'location_id': move_to_copy.location_dest_id.id,
            'location_dest_id': self.location_dest_id.id,
            'date': new_date,
            'date_expected': new_date,
            'company_id': self.company_id.id,
            'picking_id': False,
            'picking_type_id': self.picking_type_id.id,
            'propagate': self.propagate,
            'push_rule_id': self.id,
            'warehouse_id': self.warehouse_id.id,
            'partner_id': move_to_copy.picking_id.partner_id.id or ''
        }

        return new_move_vals
