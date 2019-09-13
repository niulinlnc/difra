from odoo import api, fields, models, _

import logging
_logger = logging.getLogger(__name__)

class event(models.Model):
    _inherit = ['calendar.event']

    categ_ids = fields.Many2one('calendar.event.type', string='Tag', required=True)
    
    hex_value  = fields.Char(
        string="Color value for category",
        related="categ_ids.color",
        store=False,
        size=7
    )