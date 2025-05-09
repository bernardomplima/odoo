<<<<<<< HEAD
# -*- coding: utf-8 -*-
{
    'name': "my_module",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

=======
{
    'name': 'MRP BOM Rounding Constraint',
    'version': '16.0.1.0.0',
    'summary': 'Restringe ordens de produção a múltiplos definidos na BoM',
    'description': 'Garante que a quantidade a produzir respeita o múltiplo da lista de materiais.',
    'category': 'Manufacturing',
    'author': 'Seu Nome',
    'depends': ['mrp'],
    'data': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
>>>>>>> origin/feature-1
