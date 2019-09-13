# -*- coding: utf-8 -*-
from . import account_tax

from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'



