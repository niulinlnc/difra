# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_partner_distributor = fields.Boolean(related='partner_id.distributor', string="Is a Distributor")