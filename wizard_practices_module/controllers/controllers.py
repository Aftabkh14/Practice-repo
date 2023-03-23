# -*- coding: utf-8 -*-
# from odoo import http


# class WizardPracticesModule(http.Controller):
#     @http.route('/wizard_practices_module/wizard_practices_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wizard_practices_module/wizard_practices_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('wizard_practices_module.listing', {
#             'root': '/wizard_practices_module/wizard_practices_module',
#             'objects': http.request.env['wizard_practices_module.wizard_practices_module'].search([]),
#         })

#     @http.route('/wizard_practices_module/wizard_practices_module/objects/<model("wizard_practices_module.wizard_practices_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wizard_practices_module.object', {
#             'object': obj
#         })
