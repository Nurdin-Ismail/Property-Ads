# -*- coding: utf-8 -*-
{
    'name': "Real Estate Ads",

    'summary': """
        Real Estate Module
    """,
    'author': "Nurdin",
    'website': "https://www.odoo.com",
    'category': 'Website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website', 'web'],
    'application': True,
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
        'views/property_view.xml',
        'views/property_type_view.xml',
        'views/property_tag_view.xml',
        'views/property_offer_view.xml',
        'views/menu_items.xml',
    ],
    'assets': {
        'real.assets': [
            # # bootstrap
            # ('include', 'web._assets_helpers'),
            # 'web/static/src/scss/pre_variables.scss',
            # 'web/static/lib/bootstrap/scss/_variables.scss',
            # ('include', 'web._assets_bootstrap_backend'),

            # # required for fa icons
            # 'web/static/src/libs/fontawesome/css/font-awesome.css',
            
            # # include base files from framework
            # ('include', 'web._assets_core'),

            # # remove some files that we do not use to create a minimal bundle
            # ('remove', 'web/static/src/core/**/*'),
            # ('remove', 'web/static/lib/luxon/luxon.js'),
            # 'web/static/src/core/utils/concurrency.js',
            # 'web/static/src/core/utils/strings.js',
            # 'web/static/src/core/l10n/translation.js',
            # 'web/static/src/core/utils/functions.js',
            # 'web/static/src/core/browser/browser.js',
            # 'web/static/src/core/registry.js',
            # 'web/static/src/core/assets.js',
            # 'pss/static/src/FormPage/*',
            # 'pss/static/src/*',
        ],
    },
    'license': 'AGPL-3'
}
