# (c) AbAKUS IT Solutions
import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    purchase_mode = fields.Selection([('email', 'Email'), ('fax', 'Fax'), ('paper', 'Paper'), ('phone', 'Phone'), ('webstore', 'Webstore')], string="Purchase Mode")

    @api.multi
    @api.onchange('partner_id')
    def change_purchase_mode(self):
        for order in self:
            if order.partner_id and order.partner_id.purchase_mode:
                order.purchase_mode = order.partner_id.purchase_mode

    @api.model
    def create(self, values):
        if not 'purchase_mode' in values or values['purchase_mode'] == False:
            partner_id = self.env['res.partner'].search([('id', '=', values['partner_id'])])
            values.update({
                'purchase_mode': partner_id.purchase_mode,
            })
        record = super(PurchaseOrder, self).create(values)

        return record
