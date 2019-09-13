# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)


class ClaimTag(models.Model):
    _name = "claim.tag"
    _description = "key words to sort and classify claims"

    name = fields.Char("Name", required=True)
    active = fields.Boolean("Active", default=True)
    color = fields.Integer("Color")
