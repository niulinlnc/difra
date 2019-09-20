# -*- coding: utf-8 -*-
from . import account_tax

from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)


class AccountTax(models.Model):
    _inherit = 'account.tax'

    display_detailled_line = fields.Boolean(string="Display a detailled line for this tax on the invoice report and hide it in the tax table")
    show_base_line = fields.Boolean(string="Display a base line in the tax table before the line")
