from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

import logging
_logger = logging.getLogger(__name__)

class AccountPaymentTerm(models.Model):
    _inherit = 'account.payment.term'

    @api.one
    def compute(self, value, date_ref=False):
        date_ref = date_ref or fields.Date.today()
        amount = value
        sign = value < 0 and -1 or 1
        result = []
        if self.env.context.get('currency_id'):
            currency = self.env['res.currency'].browse(self.env.context['currency_id'])
        else:
            currency = self.env.user.company_id.currency_id
        for line in self.line_ids:
            if line.value == 'fixed':
                amt = sign * currency.round(line.value_amount)
            elif line.value == 'percent':
                amt = currency.round(value * (line.value_amount / 100.0))
            elif line.value == 'balance':
                amt = currency.round(amount)
            if amt:
                next_date = fields.Date.from_string(date_ref)
                if line.option == 'day_after_invoice_date':
                    next_date += relativedelta(days=line.days)
                elif line.option == 'fix_day_following_month':
                    next_first_date = next_date + relativedelta(day=1, months=1)  # Getting 1st of next month
                    next_date = next_first_date + relativedelta(days=line.days - 1)
                elif line.option == 'last_day_following_month':
                    next_date += relativedelta(day=31, months=1)  # Getting last day of next month
                elif line.option == 'last_day_current_month':
                    next_date += relativedelta(day=31, months=0)  # Getting last day of next month
                elif line.option == 'days_after_end_of_month':
                    next_date += relativedelta(days=line.days) # add the number of days
                    next_date = next_date + relativedelta(day=1, months=1)  # Getting 1st of next month
                    next_date = next_date + relativedelta(days=-1)  # Get the last day of the previous month
                result.append((fields.Date.to_string(next_date), amt))
                amount -= amt
        amount = sum(amt for _, amt in result)
        dist = currency.round(value - amount)
        if dist:
            last_date = result and result[-1][0] or fields.Date.today()
            result.append((last_date, dist))
        return result

class AccountPaymentTermLine(models.Model):
    _inherit = 'account.payment.term.line'

    option = fields.Selection([
            ('day_after_invoice_date', "day(s) after the invoice date"),
            ('after_invoice_month', "day(s) after the end of the invoice month"),
            ('days_after_end_of_month', "day(s) at the end of the month"),
            ('day_following_month', "of the following month"),
            ('day_current_month', "of the current month"),
        ],
        default='day_after_invoice_date', required=True, string='Options'
        )
