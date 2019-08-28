# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    english_translation_created = fields.Boolean(default=False)
    
    @api.multi
    def create_translations(self):
        product_ids = self.env['product.template'].search([('english_translation_created', '=', False), '|', ('active', '=', True), ('active', '=', False), ])

        for product in product_ids:
            _logger.debug("Product : %s", product_ids)
            # check if the needed translations exists
            translated_terms_ids_1 = self.env['ir.translation'].search([('type', '=', 'model'), ('res_id', '=', product.id), ('lang', '=', 'en_US'), ('name', '=', 'product.template,name')])
            if len(translated_terms_ids_1) == 0:
                self.env['ir.translation'].create({
                    'lang': 'en_US',
                    'res_id': product.id,
                    'type': 'model',
                    'name': 'product.template,name',
                    'source': product.name,
                    'state': 'to_translate',
                })
            
            translated_terms_ids_2 = self.env['ir.translation'].search([('type', '=', 'model'), ('res_id', '=', product.id), ('lang', '=', 'en_US'), ('name', '=', 'product.template,description_sale')])
            if len(translated_terms_ids_1) == 0:
                self.env['ir.translation'].create({
                    'lang': 'en_US',
                    'res_id': product.id,
                    'type': 'model',
                    'name': 'product.template,description_sale',
                    'source': product.name,
                    'state': 'to_translate',
                })

                translated_terms_ids_2 = self.env['ir.translation'].search([('type', '=', 'model'), ('res_id', '=', product.id), ('lang', '=', 'en_US'), ('name', '=', 'product.template,description_purchase')])
            if len(translated_terms_ids_1) == 0:
                self.env['ir.translation'].create({
                    'lang': 'en_US',
                    'res_id': product.id,
                    'type': 'model',
                    'name': 'product.template,description_purchase',
                    'source': product.name,
                    'state': 'to_translate',
                })
            product.english_translation_created = True