# -*- coding: utf-8 -*-
{
    'name': "Account Invoice Texts",
    'summary': """Add header and footer texts in Invoices
    """,
    'author': "Valentin Thirion, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Purchase',
    'version': '11.0.1.1',

    'depends': [
        'purchase',
    ],

    'data': [
        'views/account_invoice_view.xml',
        'reports/account_invoice_report.xml',
    ],

    'installable': True
}