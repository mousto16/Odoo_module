# -*- coding: utf-8 -*-
{
    'name': "Real Estate",
    'summary': "Manage Real Estate",
    'version': '14.0.1',
    'depends': ['base'],
    'author': "Moustapha",
    'category': 'Estate',
    'description': """
    Our new module will cover a very specific field of activity and 
    therefore not included in the standard set of modules: real estate.
    """,
    'website': 'camersoftware.com',
    'license': 'LGPL-3',
    # data files always loaded at installation
    """'data': [
        'views/estate_view.xml',
        'security/estate_security.xml',
        'security/ir.model.access.csv',
        
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        'demo/demo_data.xml',
    ],"""
    'installable': True,
    'application': True,
    'auto_install': False,
    'price':104,
    'currency':'EUR'
}
