from odoo import models, fields

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'
    
    header_text = fields.Text(string="Optional header text")
    footer_text = fields.Text(string="Optional footer text")