# -*- encoding: utf-8 -*-
# Subject to license. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

class AccountSageCode(models.Model):
    _name = 'account.sage.code'

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Sage Export Code", required=True)

    @api.one
    def name_get(self):
        return (self.id, self.name + ' [' + self.code + ']')