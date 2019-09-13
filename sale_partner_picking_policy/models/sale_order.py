from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    @api.multi
    @api.onchange('partner_shipping_id', 'partner_id')
    def propagate_picking_policy(self):
        for order in self:
            if order.partner_shipping_id:
                order.picking_policy = order.partner_shipping_id.picking_policy
            elif order.partner_id:
                order.picking_policy = order.partner_id.picking_policy
                