from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def _action_confirm(self):
        super(SaleOrder, self)._action_confirm()
        
        for pl in self.picking_ids:
            pl.header_text = pl.sale_id.header_text
            pl.footer_text = pl.sale_id.footer_text