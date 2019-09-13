from odoo import api, fields, models, _, tools

import logging
_logger = logging.getLogger(__name__)

class calendar_event(models.Model):
    _inherit = ['calendar.event']

    mode = fields.Selection([
        ('fixed', 'Fixed timing'),
        ('variable', 'Variable timing')
    ], 'Mode', required=True, default='fixed')

    mode_text = fields.Char(string="Mode Text", compute='_compute_mode_text')

    email_options = fields.Selection([
        ('send', 'Send Email'),
        ('send_am_pm', 'Send Email with AM/PM'),
        ('noemail', 'Don\'t Send Email')
    ], 'Email Options (for non-users)', required=True, default='noemail')


    @api.multi
    def get_interval(self, interval, tz=None):

        if interval == 'time' and self._context.get('variable'):
            date = fields.Datetime.from_string(self.start)
            return _("Morning") if int(date.strftime("%-H")) < 12 else _("Afternoon")

        return super(calendar_event, self).get_interval(interval, tz)

    @api.one
    @api.depends('mode')
    def _compute_mode_text(self):
        self.mode_text = _("Variable timing") if self.mode == 'variable' else _("Fixed timing")


class calendar_attendee(models.Model):
    _inherit = ['calendar.attendee']

    @api.multi
    def _send_mail_to_attendees(self, template_xmlid='calendar_template_meeting_invitation', force_send=False):

        res = True

        for attendee in self:
            if len(self.env['res.users'].search([('partner_id', '=', attendee.partner_id.id)])) == 0:
                if attendee.event_id.email_options == 'noemail':
                    continue
                elif attendee.event_id.email_options == 'send_am_pm':
                    attendee = attendee.with_context(variable=True);

            res &= super(calendar_attendee, attendee)._send_mail_to_attendees(template_xmlid=template_xmlid, force_send=force_send)

        return res