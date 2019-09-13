# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class Partner(models.Model):
    _inherit = 'res.partner'

    intra_link_partner_ids = fields.Many2many('res.partner', 'partner_inter_link_rel', 'src_id', 'dest_id', string="Intra-partner links")