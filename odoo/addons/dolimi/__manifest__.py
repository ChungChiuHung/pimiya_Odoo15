# -*- coding: utf-8 -*-
{
    'name': "Dolimi",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "PIMIYA",
    'website': "https://github.com/PIMIYA/Odoo_15/tree/main/odoo/addons/dolimi",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory/Argriculture',
    'version': '15.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
        'views/dolimi_menu.xml',
        # 'security/ir.model.access.csv',
        # 'security/dolimi_security.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
