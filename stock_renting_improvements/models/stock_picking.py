# (c) AbAKUS IT Solutions
import logging
from odoo import models, fields, api, _

_logger = logging.getLogger(__name__)


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    rent_type = fields.Selection([('loan', 'Put on loan'), ('demo', 'Demonstration')], string="Type")
    rent_description = fields.Text(string="Description")
    rent_notes = fields.Text(string="Notes")
    rent_delivery_mode = fields.Char(string="Delivery Mode")
    is_renting = fields.Boolean(related='picking_type_id.is_renting')

    @api.multi
    @api.onchange('picking_type_id', 'partner_id')
    def change_default_note(self):
        for picking in self:
            picking_type_id = picking.picking_type_id.with_context(
                lang=picking.partner_id.lang,
            )
            picking.rent_notes = picking_type_id.renting_note