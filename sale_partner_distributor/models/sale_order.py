# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    fields.Boolean(string="test", default=False)
    
    distributor_checked = fields.Boolean(related='partner_id.distributor', string="Distributor checked")