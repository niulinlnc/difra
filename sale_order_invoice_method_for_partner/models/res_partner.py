# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

class ResPartner(models.Model):
	_inherit = 'res.partner'

	invoicing_method = fields.Selection([('per_sale', 'Once per order'), ('per_delivery', 'Once per delivery')], string='Invoicing Method', default='per_sale', required=True)
