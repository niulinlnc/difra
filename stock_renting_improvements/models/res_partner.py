# (c) AbAKUS IT Solutions
import logging
from odoo import models, fields, api, _
_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    renting_count = fields.Integer(compute='_compute_renting_count')

    @api.multi
    def _compute_renting_count(self):
        for record in self:
            domain = [
                ['partner_id', '=', record.id],
                ['picking_type_id.id', '=', self.env.ref('stock.stock_picking_type_renting_in').id],
                ['state', 'in', ('assigned', 'partially_available')]
            ]
            record.renting_count = self.env['stock.picking'].search_count(domain)

    @api.multi
    def open_rentings(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'stock.picking',
            'name': 'Rentings',
            'view_type': 'form',
            'view_mode': 'tree',
             'domain': [
                 ['partner_id', '=', self.env.context.get('partner_name')],
                 ['picking_type_id.id', '=', self.env.ref('stock.stock_picking_type_renting_in').id],
                 ['state', 'in', ('assigned', 'partially_available')]
             ]
        }
