# -*- coding: utf-8 -*-
# from odoo import http


# class BeautyShop(http.Controller):
#     @http.route('/beauty_shop/beauty_shop/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/beauty_shop/beauty_shop/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('beauty_shop.listing', {
#             'root': '/beauty_shop/beauty_shop',
#             'objects': http.request.env['beauty_shop.beauty_shop'].search([]),
#         })

#     @http.route('/beauty_shop/beauty_shop/objects/<model("beauty_shop.beauty_shop"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('beauty_shop.object', {
#             'object': obj
#         })
