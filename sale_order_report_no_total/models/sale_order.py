from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    show_total_in_report = fields.Boolean(string="Show total in report", default=True)
