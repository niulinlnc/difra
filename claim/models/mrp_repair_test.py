# -*- coding: utf-8 -*-
from odoo import models, fields

import logging
_logger = logging.getLogger(__name__)


class MrpRepairTest(models.Model):
    _name = "mrp_repair.test"

    name = fields.Char("Name", required=True)
    state = fields.Selection([('nottodo', 'Not to Do'), ('todo', 'To Do'), ('done', 'Done'), ('validated', 'Validated')], default="nottodo")
    repair_id = fields.Many2one('mrp.repair', string="Repair")
