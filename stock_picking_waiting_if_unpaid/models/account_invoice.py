# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
import logging

_logger = logging.getLogger(__name__)


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def write(self, values):
        _logger.debug("\n\nHELLO\n")
        res = super(AccountInvoice, self).write(values)
        for invoice in self:
            if 'state' in values and values['state'] == 'paid':
                order = self.env['sale.order'].search([('name', '=', invoice.origin)], limit=1)
                if order:
                    for picking in order.picking_ids:
                        picking._compute_state()
        return res
