from odoo import api, fields, models, _

import logging
_logger = logging.getLogger(__name__)

class event(models.Model):
    _inherit = ['calendar.event']

    event_suspended = fields.Boolean(string="Suspended")