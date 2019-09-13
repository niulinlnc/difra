from odoo import models, fields, api

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'
    
    @api.multi
    @api.returns('self')
    def refund(self, date_invoice=None, date=None, description=None, journal_id=None):
        # Get the refund journal if set
        if journal_id:
            journal = self.env['account.journal'].search([('id', '=', journal_id)])
            if journal and journal.refund_journal_id:
                journal_id = journal.refund_journal_id.id

        return super(AccountInvoice, self).refund(date_invoice, date, description, journal_id)