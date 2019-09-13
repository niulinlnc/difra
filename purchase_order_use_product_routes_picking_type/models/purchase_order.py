# (c) AbAKUS IT Solutions
import logging
from odoo import models, fields, api
_logger = logging.getLogger(__name__)

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.multi
    def _create_picking(self):
        StockPicking = self.env['stock.picking']
        for order in self:
            if any([ptype in ['product', 'consu'] for ptype in order.order_line.mapped('product_id.type')]):
                pickings = order.picking_ids.filtered(lambda x: x.state not in ('done', 'cancel'))
                picking_types = []
                for line in order.order_line:
                    current_picking_type_id = line.product_id.route_ids[0].pull_ids[0].picking_type_id
                    if current_picking_type_id not in picking_types:
                        picking_types.append(current_picking_type_id)
                for picking_type in picking_types:
                    filtered_pickings = pickings.filtered(lambda x: x.picking_type_id.id == picking_type.id)
                    order.picking_type_id = picking_type
                    if not filtered_pickings:
                        res = order._prepare_picking()
                        picking = StockPicking.create(res)
                    else:
                        picking = filtered_pickings[0]
                    moves = order.order_line.filtered(lambda x: x.product_id.route_ids[0].pull_ids[0].picking_type_id.id == picking_type.id)._create_stock_moves(picking)
                    moves = moves.filtered(lambda x: x.state not in ('done', 'cancel'))._action_confirm()
                    seq = 0
                    for move in sorted(moves, key=lambda move: move.date_expected):
                        seq += 5
                        move.sequence = seq
                    moves._action_assign()
                    picking.message_post_with_view('mail.message_origin_link',
                                                   values={'self': picking, 'origin': order},
                                                   subtype_id=self.env.ref('mail.mt_note').id)
        return True