# -*- encoding: utf-8 -*-
# Subject to license. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

class AccountFiscalPosition(models.Model):
    _inherit = 'account.fiscal.position'

    sage_status = fields.Selection([
        ('standard', 'Standard'),
        ('intracommunity', 'Intracommunity'),
        ('thirdcountry', 'Third Countries'),
        ('counterparty', 'Counterparty')
    ], string="Sage Fiscal Status")