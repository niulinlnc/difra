# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _
from odoo.addons import decimal_precision as dp

import logging
_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    @api.onchange('partner_invoice_id')
    def set_partner_invoice_pricelist(self):
        """
        Update the following fields when the partner is changed:
        - Pricelist
        - Payment terms
        """
        if not self.partner_invoice_id:
            self.update({
                'partner_invoice_id': False,
                'payment_term_id': False,
                'fiscal_position_id': False,
                'pricelist_id': False,
            })
            return

        values = {
            'pricelist_id': self.partner_invoice_id.property_product_pricelist and self.partner_invoice_id.property_product_pricelist.id or False,
            'payment_term_id': self.partner_invoice_id.property_payment_term_id and self.partner_invoice_id.property_payment_term_id.id or False,
        }
        self.update(values)

