# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

class ResPartner(models.Model):
	_inherit = 'res.partner'

	checked = fields.Boolean(string="Checked", default=False)
