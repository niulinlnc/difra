# -*- coding: utf-8 -*-
{
    'name': "Stock Picking Waiting If Unpaid",
    'summary': """Put stock picking in waiting if invoice is not paid  
    """,
    'author': "ABAKUS IT-SOLUTIONS",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Stock',
    'version': '11.0.1.1',

    'depends': [
        'sale',
        'account_invoicing'
    ],

    'data': [
        'views/account_payment_term.xml',
        'views/sale_order.xml'
    ],

    'installable': True
}