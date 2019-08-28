# -*- coding: utf-8 -*-
{
    'name': "Sequenced ID for Product",

    'summary': """
        Add an automatic sequence on the Internal Reference product.product
    """,

    'description': """
        Sequenced Reference for code for Product

        This module adds an automatically sequenced code for the Internal Reference on each product.
        This field will be automatically incremented using a defined sequence.

        This module has been developed by Jason PINDAT, intern @ AbAKUS it-solutions.
    """,

    'author': "Jason Pindat, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Sale',
    'version': '10.0.1.0',
    'depends': [
        'base',
        'product'
    ],
    'data': [
        'data/sequence.xml',
    ],
    
    'installable': True
}