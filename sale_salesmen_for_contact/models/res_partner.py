# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class Partner(models.Model):
    _inherit = 'res.partner'

    user_id = fields.Many2one('res.users', string='Salesperson', help='The internal user that is in charge of communicating with this contact if any.', default=lambda self: self.env.user)