# -*- coding: utf-8 -*-
# from odoo import http


# class Module-2(http.Controller):
#     @http.route('/mo_football/mo_football/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mo_football/mo_football/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mo_football.listing', {
#             'root': '/mo_football/mo_football',
#             'objects': http.request.env['mo_football.mo_football'].search([]),
#         })

#     @http.route('/mo_football/mo_football/objects/<model("mo_football.mo_football"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mo_football.object', {
#             'object': obj
#         })
