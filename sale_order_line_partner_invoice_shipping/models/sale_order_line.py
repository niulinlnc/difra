from odoo import models, fields

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    partner_invoice_id = fields.Many2one(related='order_id.partner_invoice_id', string="Invoice Address")
    partner_shipping_id = fields.Many2one(related='order_id.partner_shipping_id', string="Delivery Address")