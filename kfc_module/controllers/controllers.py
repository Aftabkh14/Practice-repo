# -*- coding: utf-8 -*-
# from odoo import http


# class KfcModule(http.Controller):
#     @http.route('/kfc_module/kfc_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kfc_module/kfc_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kfc_module.listing', {
#             'root': '/kfc_module/kfc_module',
#             'objects': http.request.env['kfc_module.kfc_module'].search([]),
#         })

#     @http.route('/kfc_module/kfc_module/objects/<model("kfc_module.kfc_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kfc_module.object', {
#             'object': obj
#         })
