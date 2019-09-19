# (c) AbAKUS IT Solutions
import logging
from odoo import models, fields, api, _, exceptions
_logger = logging.getLogger(__name__)


class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    name = fields.Char(default=lambda x: x._compute_serial_number())

    @api.multi
    @api.onchange('product_id')
    def _compute_serial_number(self):
        for lot in self:
            if not lot.product_id and not lot.product_id.default_code:
                raise exceptions.ValidationError(_("A Product must be selected"))
            else:
                if self.env.context.get('default_name'):
                    lot.name = self.env.context.get('default_name')
                else:
                    lot.name = lot.product_id.default_code.strip('0').zfill(5) + self.env['ir.sequence'].next_by_code('stock.lot.serial')
