# -*- coding: utf-8 -*-
{
    'name': "Product Report",

    'summary': """
    """,

    'description': """
        Product Report

        It adds a report on the product (template) based on the 'difra catalog view'
        It adds a button on the product to print the report
        It adds a checkbox in the sale order lines to join the report of the given product to the SO when printed

        On this report there will be printed the 'website_description' which is a rich (HTML) field that is basically the webpage presented online. This description is printed on this report as a main bloc.
        
        This module has been developed by Valentin THIRION @ AbAKUS it-solutions.
    """,

    'author': "Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Sale',
    'version': '10.0.1.0',

    'depends': [
        'sale',
        'website_sale',
    ],
    'installable': True,
    'data': [
        'wizards/product_print_report_wizard.xml',
        'views/product_view.xml',
        'views/sale_order_view.xml',
        'reports/external_layout_footer.xml',
        'reports/product_report.xml',
        'reports/sale_order_report.xml',
    ],
    'css': [
        'static/src/css/style.css',
        'static/src/css/limerick-serial-light-regular-webfont.css',
    ]
}

