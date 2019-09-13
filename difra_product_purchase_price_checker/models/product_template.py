# -*- coding: utf-8 -*-
from odoo import models, fields, api

import logging

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.multi
    def product_check_prices(self):
        with open('/home/ubuntu/test.txt', 'w') as file:
            for template in self.env['product.template'].search([]):
                history_ids = self.env['product.price.history'].search(
                    [('product_id.product_tmpl_id.id', '=', template.id)], order='datetime DESC', limit=1)
                if round(template.standard_price, 4) != round(history_ids.cost, 4):
                    _logger.critical("\nSP: %s -> History: %s", template.standard_price, history_ids.cost)
                    file.write(
                        "Prod: {} - SP: {} -> History: {}\n".format(template.default_code, template.standard_price,
                                                                    history_ids.cost))
