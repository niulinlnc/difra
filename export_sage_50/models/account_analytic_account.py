# -*- encoding: utf-8 -*-
# Subject to license. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

class AnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'
    
    sage_50_analytic_code = fields.Char()
