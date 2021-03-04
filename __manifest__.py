# -*- coding: utf-8 -*-
{
    'name': "pos_hide_options",

    'summary': """
        Hide Cash Control on POS. 
        Factura Sempai""",

    'description': """
        This module hides cash control on pos. 
    """,

    'author': "Sempai Space",
    'website': "http://www.sempai.space",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','point_of_sale',],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
#        'views/views.xml',
        'views/pos_session_view.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}
