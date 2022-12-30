# -*- coding: utf-8 -*-
{
    'name': "Football Management",

    'summary': """
        Manage footbal club, player""",

    'description': """
        Manage footbal club, player
    """,

    'author': "EM Duong",
    'website': "https://www.facebook.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'security/players_security.xml',
        'security/ir.model.access.csv',
        'views/clubs_view.xml',
        'views/players_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'images' : [
        'static/description/main_screenshot.png'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 1.0,
    'currency': 'EUR',
    'license': 'OPL-1',
}
