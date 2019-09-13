# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

import datetime
import pytz
import logging
_logger = logging.getLogger(__name__)
    
    
class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    price_history_count = fields.Integer(string="Price History Count", compute='_compute_price_history_count')
    cost_price_last_update_text = fields.Char(string="Last Cost Price Update", compute='_compute_cost_price_last_update')
    
    @api.one
    def _compute_price_history_count(self):
        self.price_history_count = len(self.env['product.price.history'].search([('product_id.product_tmpl_id.id', '=', self.id)]))

    @api.one
    def _compute_cost_price_last_update(self):
        history_ids = self.env['product.price.history'].search([('product_id.product_tmpl_id.id', '=', self.id)], order='datetime DESC', limit=1)
        if len(history_ids) == 0:
            self.cost_price_last_update_text = str("Never")
        else:
            last_update = history_ids.datetime
            local_tz = pytz.timezone(self.env.user.tz)
            d = pytz.utc.localize(datetime.datetime.strptime(history_ids.datetime, DEFAULT_SERVER_DATETIME_FORMAT)).astimezone(local_tz)
            self.cost_price_last_update_text = str(datetime.datetime.strftime(d, '%Y-%m-%d %H:%M:%S'))
        