# -*- coding: utf-8 -*-
{
    'name': 'Professional REST API',
    'version': '12.0.1.14.8',
    'category': 'Extra Tools',
    'author': 'AVS SP',
    'support': 'avs3.ua@gmail.com',
    'license': 'OPL-1',
    'website': 'https://rest-api-demo.dsdatacloud.de',
    'price': 129.00,
    'currency': 'EUR',
    'summary': """Professional RESTful API access to Odoo models with (optional) predefined and tree-like schema of response Odoo fields
        ========================================================================
        Tags: restapi, connector, connection, integration, endpoint, endpoints, route, routes, call method, calling method, openapi, oauth, swagger, webhook, webhooks, report, reports
        """,
    'live_test_url': 'https://app.swaggerhub.com/apis-docs/avs3/odoo_rest_api/1',
    'external_dependencies': {
        'python': ['simplejson'],
    },
    'depends': [
        'base',
        'web',
    ],
    'data': [
        'data/ir_configparameter_data.xml',
        'data/ir_cron_data.xml',
        'security/ir.model.access.csv',
        'views/ir_model_view.xml',
    ],
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
