from odoo import models, fields

class sale_order_improvements(models.Model):
    _inherit = 'sale.order.line'
    
    comment_text = fields.Text(string="Optional comment text")
    display_position = fields.Selection([('before', 'Before line'), ('after', 'After line')], string="Display comment text", default='before')