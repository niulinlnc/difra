# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

class SaleOrder(models.Model):
	_inherit = 'sale.order'

	partner_sale_order_comment = fields.Text(related='partner_id.sale_order_comment')