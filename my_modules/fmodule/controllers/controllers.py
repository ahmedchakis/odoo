# -*- coding: utf-8 -*-
# from odoo import http


# class Fmodule(http.Controller):
#     @http.route('/fmodule/fmodule', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fmodule/fmodule/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fmodule.listing', {
#             'root': '/fmodule/fmodule',
#             'objects': http.request.env['fmodule.fmodule'].search([]),
#         })

#     @http.route('/fmodule/fmodule/objects/<model("fmodule.fmodule"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fmodule.object', {
#             'object': obj
#         })
