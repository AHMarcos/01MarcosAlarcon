# -*- coding: utf-8 -*-
# from odoo import http


# class AhmarcosModule(http.Controller):
#     @http.route('/ahmarcos_module/ahmarcos_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ahmarcos_module/ahmarcos_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ahmarcos_module.listing', {
#             'root': '/ahmarcos_module/ahmarcos_module',
#             'objects': http.request.env['ahmarcos_module.ahmarcos_module'].search([]),
#         })

#     @http.route('/ahmarcos_module/ahmarcos_module/objects/<model("ahmarcos_module.ahmarcos_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ahmarcos_module.object', {
#             'object': obj
#         })
