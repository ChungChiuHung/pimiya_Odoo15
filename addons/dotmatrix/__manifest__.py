# -*- coding: utf-8 -*-
{
    'name': "dotmatrix",

    'summary': """
        Odoo dot matrix print for many dolimi agriculture applications""",

    'description': """
        Dolimi dot matrix print, for logistics, warehouse, agriculture, etc.
    """,

    'author': "PIMIYA",
    'website': "https://github.com/PIMIYA/Odoo_15",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Operations/Agriculture',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'sale', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/stock_picking.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
