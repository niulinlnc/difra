# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

class ProductTemplate(models.Model):
	_inherit = 'product.template'

	checked = fields.Boolean('Checked')
