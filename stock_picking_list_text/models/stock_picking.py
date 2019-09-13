from odoo import models, fields

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    header_text = fields.Text(string="Optional header text")
    footer_text = fields.Text(string="Optional footer text")
