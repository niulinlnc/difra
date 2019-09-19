from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class AccountPaymentTerm(models.Model):
    _inherit = 'account.payment.term'

    payment_before_delivery = fields.Boolean("Payment Before Delivery", default=False)
