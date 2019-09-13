from odoo import api, fields, models, _

import logging
_logger = logging.getLogger(__name__)

class event_type(models.Model):
    _inherit = ['calendar.event.type']
    _order = 'name'

    color = fields.Char(string="Color", help="Choose your color", size=7)
    active = fields.Boolean(default=True)

    # @api.multi
    # def deactivate(self):
    #     self.active = False
    #     return False