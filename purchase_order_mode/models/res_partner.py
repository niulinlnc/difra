# (c) AbAKUS IT Solutions
import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class Partner(models.Model):
    _inherit = 'res.partner'

    purchase_mode = fields.Selection([('email', 'Email'), ('fax', 'Fax'), ('paper', 'Paper'), ('phone', 'Phone'), ('webstore', 'Webstore')], string="Purchase Mode")
