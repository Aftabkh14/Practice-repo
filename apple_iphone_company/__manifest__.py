# -*- coding: utf-8 -*-
{
    'name': "apple_iphone_company",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizadii/apple_new_wizard.xml',
        'views/views.xml',
        'views/mac.xml',
        'views/ipad.xml',
        'views/iphone.xml',
        'views/wacth.xml',
        'views/airpods.xml',
        'views/compare_apple.xml',
        'views/male_female_new.xml',
        'report/iphone_report_action.xml',
        'report/iphone_report_temp.xml',
        'report/apple_python_report_actionl.xml',
        'report/apple_python_temp_report.xml',
        'report/sale_action.xml',
        'report/sale_temp.xml',
        # 'report/paper_format_action.xml',
        # 'report/paper_format_temp.xml',
        # 'report/inherited_report_temp.xml',
        'views/templates.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
