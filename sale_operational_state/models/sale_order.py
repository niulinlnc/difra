# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    operational_state = fields.Selection([
        ('draft', _('Draft')),
        ('to_produce', _('To produce')),
        ('to_send', _('To send')),
        ('to_invoice', _('To invoice')),
        ], string='Operational State', index=True, track_visibility='onchange', default='draft')