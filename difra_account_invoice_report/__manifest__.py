# -*- coding: utf-8 -*-
{
    'name': "DIFRA : Account Invoice Report",

    'summary': """
    """,

    'author': "Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Sale',
    'version': '11.0.1.0',

    'depends': [
        'account',
        'claim',
    ],

    'data': [
        'views/account_tax.xml',

        'reports/account_invoice_report.xml',
    ],
}
