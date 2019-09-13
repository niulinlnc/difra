# -*- coding: utf-8 -*-
""" Custom processing for our report
"""
import logging
from odoo import api, models, _
from odoo.exceptions import UserError
from pprint import pformat
_logger = logging.getLogger(__name__)


class ReportProduct(models.AbstractModel):
    _name = 'report.product_report.report_product_template'

    @api.model
    def get_report_values(self, docids, data=None):

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'selected_lang': data['form']['lang'],
            'docs': self.env['product.template'].search([('id', '=', data['form']['product_tmpl_id'])]),
        }
