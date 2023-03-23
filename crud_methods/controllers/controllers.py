# -*- coding: utf-8 -*-
# from odoo import http


# class CrudMethods(http.Controller):
#     @http.route('/crud_methods/crud_methods/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crud_methods/crud_methods/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('crud_methods.listing', {
#             'root': '/crud_methods/crud_methods',
#             'objects': http.request.env['crud_methods.crud_methods'].search([]),
#         })

#     @http.route('/crud_methods/crud_methods/objects/<model("crud_methods.crud_methods"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crud_methods.object', {
#             'object': obj
#         })
