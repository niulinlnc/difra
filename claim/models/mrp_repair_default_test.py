# -*- coding: utf-8 -*-
from odoo import models, fields

import logging
_logger = logging.getLogger(__name__)


class MrpRepairDefaultTest(models.Model):
    _name = "mrp_repair.default_test"

    name = fields.Char("Name", required=True)
