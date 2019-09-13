# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
from odoo import models, fields, api, _
from odoo.exceptions import UserError

import logging
_logger = logging.getLogger(__name__)


class MrpProductProduce(models.TransientModel):
    _inherit = 'mrp.product.produce'

    @api.multi
    def do_produce(self):
        if any([line.qty_done == 0 for line in self.produce_line_ids]):
            raise UserError(_("You need to fill 'Done' quantities before recording the production."))
        return super(MrpProductProduce, self).do_produce()
