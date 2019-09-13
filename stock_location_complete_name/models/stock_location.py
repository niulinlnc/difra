# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

import logging
_logger = logging.getLogger(__name__)

class StockLocation(models.Model):
    _inherit = 'stock.location'
    _order = 'parent_left, name'

    @api.multi
    def name_get(self):
        ret_list = []
        for location in self:
            orig_location = location
            name = location.name
            while location.location_id:
                location = location.location_id
                name = location.name + " / " + name
            ret_list.append((orig_location.id, name))
        return ret_list