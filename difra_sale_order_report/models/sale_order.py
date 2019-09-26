# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
from odoo.addons import decimal_precision as dp
from datetime import datetime
import logging

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    pro_forma_description = fields.Text(string="Pro-Forma Informations", store=True, default="Payment with BELFIUS BANK WELKENRAEDT\nSwift: GKCCBEBB\nAccount no. : 776-5993591-58\nIBAN BE95 7765 9935 9158\nAll bank costs to your charge")
