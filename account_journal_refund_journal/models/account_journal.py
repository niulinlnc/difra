from odoo import models, fields

class AccountJournal(models.Model):
    _inherit = 'account.journal'
    
    refund_journal_id = fields.Many2one('account.journal', string="Journal for refunds", help="Specify here a journal for refunds if you don't want to have refunds in this journal")