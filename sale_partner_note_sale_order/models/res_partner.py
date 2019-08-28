# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

class ResPartner(models.Model):
	_inherit = 'res.partner'

	sale_order_comment = fields.Text(string="Comment for Sale Order")