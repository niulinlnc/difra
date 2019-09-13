# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)


class MrpProductProduce(models.TransientModel):
    _inherit = 'mrp.product.produce'

    life_date = fields.Datetime("End of Life Date", related='lot_id.life_date')

    @api.onchange('produce_line_ids')
    def _onchange_produce_line_ids(self):
        for produce in self:
            for line in produce.produce_line_ids:
                if line.lot_id and line.lot_id.life_date:
                    line.life_date = line.lot_id.life_date
