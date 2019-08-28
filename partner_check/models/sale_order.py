# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

class SaleOrder(models.Model):
	_inherit = 'sale.order'

	partner_checked = fields.Boolean(related='partner_id.checked', string="Partner checked")