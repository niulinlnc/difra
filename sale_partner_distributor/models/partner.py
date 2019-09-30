# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

class Partner(models.Model):
    _inherit = 'res.partner'

    # Add a new column to the res.partner model, by default partners are not
    # instructors
    distributor = fields.Boolean(string="Is a distributor", default=False)

    distributor_id = fields.Many2one('res.partner', string="Distributor")

    finalclient_ids = fields.One2many('res.partner', 'distributor_id', string="Final clients", readonly = True)

    # Not working
    #@api.onchange('distributor')
    #def _onDistributor_change(self):
    #    if self.distributor:
    #        self.distributor_id = False