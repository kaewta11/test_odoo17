# -*- coding: utf-8 -*-
{
    'name': 'Exchange Rate sync',
    'version': '1.0',
    'category': '',
    'description': """

    """,
    'author': '',
    'website': '',
    'depends': ['base', 'account'],

    'data': [
        'security/ir.model.access.csv',
        'views/account_invoice_views.xml',
        'wizard/wizard_exchange_rate_sync_view.xml',
        
    ],

    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'images': [],
}
