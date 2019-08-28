# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _
import time
from datetime import date, datetime
import logging
_logger = logging.getLogger(__name__)

class SaleOrderWithMethod(models.Model):
    _inherit = 'sale.order'
    
    invoicing_method = fields.Selection([('per_sale', 'Once per order'), ('per_delivery', 'Once per delivery')], string='Invoicing Method', default=lambda self: self._get_partner_invoicing_method(), required=True)

    def _get_partner_invoicing_method(self):
        if self.partner_id:
            return self.partner_id.invoicing_method
        return 'per_sale'

    @api.onchange('partner_id')
    def _change_invoicing_method(self):
        if self.partner_id:
            self.invoicing_method = self.partner_id.invoicing_method

    @api.depends('state', 'order_line.invoice_status')
    def _get_invoiced(self):
        """
        Compute the invoice status of a SO. Possible statuses:
        - no: if the SO is not in status 'sale' or 'done', we consider that there is nothing to
          invoice. This is also hte default value if the conditions of no other status is met.
        - to invoice:
            - if the sale has for invoicing method 'per_sale' :
                - if all the lines are set as 'to invoice', the whole SO is 'to invoice'
                - if not : SO is set as 'no'
            - if the sale has for invoicing method 'per_delivery' :
                - if any SO line is 'to invoice', the whole SO is 'to invoice' (We kept behavior as default)
        - invoiced: if all SO lines are invoiced, the SO is invoiced.
        - upselling: if all SO lines are invoiced or upselling, the status is upselling.
        The invoice_ids are obtained thanks to the invoice lines of the SO lines, and we also search
        for possible refunds created directly from existing invoices. This is necessary since such a
        refund is not directly linked to the SO.
        """
        for order in self:
            invoice_ids = order.order_line.mapped('invoice_lines').mapped('invoice_id').filtered(lambda r: r.type in ['out_invoice', 'out_refund'])
            # Search for invoices which have been 'cancelled' (filter_refund = 'modify' in
            # 'account.invoice.refund')
            # use like as origin may contains multiple references (e.g. 'SO01, SO02')
            refunds = invoice_ids.search([('origin', 'like', order.name), ('company_id', '=', order.company_id.id)]).filtered(lambda r: r.type in ['out_invoice', 'out_refund'])
            invoice_ids |= refunds.filtered(lambda r: order.name in [origin.strip() for origin in r.origin.split(',')])
            # Search for refunds as well
            refund_ids = self.env['account.invoice'].browse()
            if invoice_ids:
                for inv in invoice_ids:
                    refund_ids += refund_ids.search([('type', '=', 'out_refund'), ('origin', '=', inv.number), ('origin', '!=', False), ('journal_id', '=', inv.journal_id.id)])

            # Ignore the status of the deposit product
            deposit_product_id = self.env['sale.advance.payment.inv']._default_product_id()
            line_invoice_status = [line.invoice_status for line in order.order_line if line.product_id != deposit_product_id]

            # Basic case based on state
            if order.state not in ('sale', 'done'):
                invoice_status = 'no'
            else:
                if order.invoicing_method == 'per_sale' and all(invoice_status == 'to invoice' for invoice_status in line_invoice_status):
                    invoice_status = 'to invoice'

                elif order.invoicing_method == 'per_month' and any(invoice_status == 'to invoice' for invoice_status in line_invoice_status) and invoiced_this_month == False:
                    invoice_status = 'to invoice'

                elif order.invoicing_method == 'per_delivery' and any(invoice_status == 'to invoice' for invoice_status in line_invoice_status):
                    invoice_status = 'to invoice'

                elif all(invoice_status == 'invoiced' for invoice_status in line_invoice_status):
                    invoice_status = 'invoiced'

                elif all(invoice_status in ['invoiced', 'upselling'] for invoice_status in line_invoice_status):
                    invoice_status = 'upselling'

                else:
                    invoice_status = 'no'

            order.update({
                'invoice_count': len(set(invoice_ids.ids + refund_ids.ids)),
                'invoice_ids': invoice_ids.ids + refund_ids.ids,
                'invoice_status': invoice_status
            })

    @api.multi
    def action_invoice_create(self, grouped=False, final=False):
        return super(SaleOrderWithMethod, self).action_invoice_create(grouped, final)