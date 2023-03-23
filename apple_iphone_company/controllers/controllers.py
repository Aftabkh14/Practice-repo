# -*- coding: utf-8 -*-
# from odoo import http


# class AppleIphoneCompany(http.Controller):
#     @http.route('/apple_iphone_company/apple_iphone_company/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/apple_iphone_company/apple_iphone_company/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('apple_iphone_company.listing', {
#             'root': '/apple_iphone_company/apple_iphone_company',
#             'objects': http.request.env['apple_iphone_company.apple_iphone_company'].search([]),
#         })

#     @http.route('/apple_iphone_company/apple_iphone_company/objects/<model("apple_iphone_company.apple_iphone_company"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('apple_iphone_company.object', {
#             'object': obj
#         })
