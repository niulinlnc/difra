# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)


class ProcurementGroup(models.Model):
    _inherit = 'procurement.group'

    @api.model
    def _run_scheduler_tasks(self, use_new_cursor=False, company_id=False):
        nb_mo = -1
        new_nb_mo = self.env['mrp.production'].search_count([('state','in',('confirmed', 'planned', 'progress'))])
        while new_nb_mo > nb_mo:
            super(ProcurementGroup, self)._run_scheduler_tasks(use_new_cursor, company_id)
            nb_mo = new_nb_mo
            new_nb_mo = self.env['mrp.production'].search_count([('state','in',('confirmed', 'planned', 'progress'))])
