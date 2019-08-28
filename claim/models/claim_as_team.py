# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)


class ClaimASTeam(models.Model):
    _name = "claim.as_team"
    _description = ""

    name = fields.Char("Name")
    active = fields.Boolean("Active", default=True)

    as_responsible_id = fields.Many2one('res.users', string="AS Responsible")
    quality_responsible_id = fields.Many2one('res.users', string="Quality Responsible")
    member_ids = fields.Many2many('res.users', string="Members")
    claim_ids = fields.One2many('claim', 'team_id', string="Related Claims", readonly="1")
