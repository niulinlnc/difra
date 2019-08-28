# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

class Product(models.Model):
	_inherit = 'product.template'

	rich_description = fields.Html("Rich Description", translate=True)