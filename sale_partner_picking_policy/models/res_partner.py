from odoo import models, fields

class Partner(models.Model):
    _inherit = 'res.partner'
    
    picking_policy = fields.Selection([
        ('direct', 'Deliver each product when available'),
        ('one', 'Deliver all products at once')],
        string='Shipping Policy', default='one')
