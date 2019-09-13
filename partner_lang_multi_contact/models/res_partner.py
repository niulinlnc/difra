# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.multi
    @api.onchange('lang')
    def populateLang(self):
        for partner in self:
            # Upper partner
            if partner.contact_id:
                partner.contact_id.lang = partner.lang
            # Other functions
            for function in partner.other_contact_ids:
                function.lang = partner.lang