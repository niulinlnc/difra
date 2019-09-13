# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

class ResPartner(models.Model):
	_inherit = 'res.partner'

	checked_date = fields.Date(string="Check date")
