# (c) AbAKUS IT Solutions
import logging
from odoo import models, fields, api
_logger = logging.getLogger(__name__)

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    @api.multi
    def _prepare_stock_moves(self, picking):
        res = super(PurchaseOrderLine, self)._prepare_stock_moves(picking)
        picking_type_id = self.product_id.route_ids[0].pull_ids[0].picking_type_id
        if len(res) > 0:
            res[0]['picking_type_id'] = picking_type_id.id
            res[0]['route_ids'] = picking_type_id.warehouse_id and [(6, 0, [x.id for x in picking_type_id.warehouse_id.route_ids])] or []
            res[0]['warehouse_id'] = picking_type_id.warehouse_id.id
        return res
