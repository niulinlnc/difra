# (c) AbAKUS IT Solutions
import logging
from odoo import models, fields, api, _
from datetime import date
from datetime import timedelta

_logger = logging.getLogger(__name__)


class CalendarEvent(models.Model):
    _inherit = ['calendar.event']

    attachments_count_text = fields.Char(compute='_compute_attachments_count_text', string="Attachment(s) count")

    def _compute_attachments_count_text(self):
        for event in self:
            count = len(self.env['ir.attachment'].search([('res_model', '=', 'calendar.event'), ('res_id', '=', event.id)]))
            if count > 0:
                event.attachments_count_text = str(count) + _(' files attached')
            else:
                event.attachments_count_text = str('No files attached')
                