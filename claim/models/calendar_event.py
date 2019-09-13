# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    claim_id = fields.Many2one('claim', string="Claim")
    repair_id = fields.Many2one('mrp.repair', string="Repair", readonly=True, related='claim_id.repair_id')

    @api.onchange('claim_id')
    def _change_repair_id(self):
        self.repair_id = self.claim_id.repair_id or self.env['mrp.repair'].id
