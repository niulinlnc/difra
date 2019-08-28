from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    
    header_text = fields.Text(string="Optional header text")
    footer_text = fields.Text(string="Optional footer text")