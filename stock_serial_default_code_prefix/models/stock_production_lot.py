# (c) AbAKUS IT Solutions
import logging
from odoo import models, fields, api, _, exceptions
_logger = logging.getLogger(__name__)


class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    name = fields.Char(default="New", compute="_compute_serial_number", store=True)

    @api.multi
    @api.onchange('product_id')
    def _compute_serial_number(self):
        for lot in self:
            if not lot.product_id and not lot.product_id.default_code:
                raise exceptions.ValidationError(_("A Product must be selected"))
            else:
                lot['name'] = lot.product_id.default_code.strip('0').zfill(5) + self.env['ir.sequence'].next_by_code('stock.lot.serial')
