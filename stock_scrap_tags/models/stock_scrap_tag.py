# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class StockScrapTag(models.Model):
    _name = 'stock.scrap.tag'

    name = fields.Char(string="Name", required=True)
    active = fields.Boolean("Active", default=True)
