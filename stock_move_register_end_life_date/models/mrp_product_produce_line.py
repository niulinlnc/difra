# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)


class MrpProductProduceLine(models.TransientModel):
    _inherit = 'mrp.product.produce.line'

    life_date = fields.Datetime("End of Life Date", related='lot_id.life_date')

    @api.onchange('lot_id')
    def _onchange_lot_id(self):
        res = super(MrpProductProduceLine, self)._onchange_lot_id()
        if self.lot_id.life_date:
            self.life_date = self.lot_id.life_date
        return res
