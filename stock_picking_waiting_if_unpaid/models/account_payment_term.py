# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
import logging

_logger = logging.getLogger(__name__)


class AccountPaymentTerm(models.Model):
    _inherit_id = 'account.payment.term'

    payment_before_delivery = fields.Boolean("Payment Before Delivery", default=False)
