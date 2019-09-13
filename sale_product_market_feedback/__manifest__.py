# -*- coding: utf-8 -*-
{
    'name': "Sale Product Market Feedback",

    'summary': """
    """,

    'description': """
        Sale Product Market Feedback

        This module provides a way to add feedbacks from the market to a product. (e.g. This product might be blue instead of red)
        
        This module has been developed by François WYAIME @ AbAKUS it-solutions.
    """,

    'author': "François WYAIME, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Sale',
    'version': '11.0.1.0',

    'depends': ['base', 'sale', 'product'],

    'data': [
        'security/ir.model.access.csv',

        'views/product_market_feedback.xml',
        'views/product_template.xml',
        'views/product_category.xml'
    ],
}