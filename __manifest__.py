# -*- coding: utf-8 -*-
{
    'name': "Custom Invoices",

    'summary': """Companys invoices Costa rica""",

    'description': """

    """,

    'author': "Adrian Cordoba",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'account_invoices',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        'reports/consurba_invoice.xml',
        'reports/berny_invoice.xml',
        'reports/mariella_invoice.xml',
        'reports/rdiaz_invoice.xml'
    ]
}