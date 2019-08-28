# -*- coding: utf-8 -*-
{
    'name': "Print multiple Reports Copies for Partners",
    'description': """
        Print multiple Reports Copies for Partners

        This module adds 3 int fields on the partner form (#of copies for SO, PO and Invoice).
        This number (default = 1) will be used to directly export in PDF (or print) this number of copies of the report.

        This module has been developed by Valentin THIRION @ AbAKUS it-solutions.
    """,

    'author': "Valentin Thirion, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Sale',
    'version': '10.0.1.0',
    'depends': [
        'sale',
    ],
    'data': [
        'views/partner_views.xml',
        'reports/sale_order_reports.xml',
        'reports/purchase_order_reports.xml',
        'reports/invoice_reports.xml',
    ],
    
    'installable': True
}