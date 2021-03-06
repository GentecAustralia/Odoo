# -*- coding: utf-8 -*-


{
    'name': 'Auto-removal of account.invoice followers',
    'version': '12.0.0.0',
    'category': 'Accounting',
    'summary': """
        This apps automatically remove followers of account.invoice.
    """,
    'description': """
        This apps automatically remove followers of account.invoice
    """,
    'depends': [
        'account',
        'sale_management',
        'purchase'
    ],
    'data': [
    ],
    'installable': True,
    'auto_install': False,
}
