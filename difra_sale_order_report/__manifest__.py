# -*- coding: utf-8 -*-
{
    'name': "DIFRA : Sale Order Report",

    'summary': """
    """,

    'author': "Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Sale',
    'version': '11.0.1.0',

    'depends': [
        'base',
        'sale'
    ],

    'data': [
        'views/res_company_form.xml',

        'reports/sale_order_template.xml',
    ],
}