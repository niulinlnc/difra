# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    distributor = fields.Boolean(string="Is a Distributor", default=False)
    distributor_id = fields.Many2one('res.partner', string="Distributor")
    final_customer_ids = fields.One2many('res.partner', 'distributor_id', string="Final Customers", readonly = True)