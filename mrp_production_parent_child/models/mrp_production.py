# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

import logging
_logger = logging.getLogger(__name__)


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    parent_mo_id = fields.Many2one('mrp.production', string="Finished Poduct")
    is_parent = fields.Boolean(string="Is a finished product", readonly=True)

    # @api.one
    # def _compute_is_parent(self):
    #     self.ensure_one()
    #     self.is_parent = self.parent_mo_id.id == self.id
