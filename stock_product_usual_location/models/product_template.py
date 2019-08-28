# (c) AbAKUS IT Solutions
import logging
from odoo import models, fields, api, _

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    usual_stock_location_info = fields.Char(string="Usual stock location", help="This text will be printed alongside stock picking reports to help the stock maintainer for his work")
