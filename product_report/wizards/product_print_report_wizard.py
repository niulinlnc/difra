# -*- coding: utf-8 -*-
""" Print wizard for rapport language selection
"""
import logging
from odoo import api, fields, models, _
_logger = logging.getLogger(__name__)


class ProductReportPrintWizard(models.TransientModel):
    """ Main wizard class """
    _name = 'product.report.print.wizard'
    _description = 'Product Report Wizard'

    product_tmpl_id = fields.Many2one('product.template', 'Template', required=True)
    lang = fields.Many2one('res.lang', 'Language', required=True)

    @api.model
    def default_get(self, fields):
        """ Make sure we pre-fill the product_tmp_id with the proper value apssed through context """
        res = super(ProductReportPrintWizard, self).default_get(fields)
        if not res.get('default_product_template_id') and self.env.context.get('active_id') and self.env.context.get(
                'active_model') == 'product.template':
            res['product_tmpl_id'] = self.env['product.template'].search([('id', '=', self.env.context['active_id'])],
                                                                         limit=1).id

        elif res.get('default_product_template_id') and self.env.context.get('active_model') == 'product.template':
            res['product_tmpl_id'] = self.env['product.template'].browse(
                self.env.context['default_product_template_id']).id
        return res

    @api.multi
    def get_report(self):
        """ load data from the form """
        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {
                'product_tmpl_id': self.product_tmpl_id.id,
                'lang': self.lang.iso_code,
            },
        }
        
        return self.env.ref('product_report.report_product').report_action(self, data=data, config=False)

    