# (c) AbAKUS IT Solutions
import base64

from odoo import models, fields, api, tools, _
from odoo.modules.module import get_module_resource

import logging
_logger = logging.getLogger(__name__)


class CalendarEvent(models.Model):
    _inherit = ['calendar.event']

    attachments_count_text = fields.Char(compute='_compute_attachments_count_text', string="Attachment(s) count")
    attachments_count = fields.Integer(compute='_compute_attachments_count', string="Attachment(s) count")
    attachments_image = fields.Binary(string='Attachments image', default=lambda self:self._get_default_image())
    attachment_ids = fields.Many2one('ir.attachment', compute='_compute_attachments', string='Attachments', )

    @api.model
    def _get_default_image(self, colorize=False):
        img_path = get_module_resource('calendar_event_attachments_flag', 'static/src/img', 'ribbon.png')
        if img_path:
            with open(img_path, 'rb') as f:
                image = f.read()

        return tools.image_resize_image_big(base64.b64encode(image))

    def _compute_attachments(self):
         for event in self:
            event.attachment_ids = (6, 0, [self.env['ir.attachment'].search([('res_model', '=', 'calendar.event'), ('res_id', '=', event.id)])])

    def _compute_attachments_count_text(self):
        for event in self:
            count = len(self.env['ir.attachment'].search([('res_model', '=', 'calendar.event'), ('res_id', '=', event.id)]))
            if count > 0:
                event.attachments_count_text = str(count) + _(' files attached')
            else:
                event.attachments_count_text = str('No files attached')

    def _compute_attachments_count(self):
        for event in self:
            event.attachments_count = len(event.attachment_ids)