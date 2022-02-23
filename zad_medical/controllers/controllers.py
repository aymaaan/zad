# -*- coding: utf-8 -*-
# from odoo import http


# class ZadMedical(http.Controller):
#     @http.route('/zad_medical/zad_medical', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zad_medical/zad_medical/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('zad_medical.listing', {
#             'root': '/zad_medical/zad_medical',
#             'objects': http.request.env['zad_medical.zad_medical'].search([]),
#         })

#     @http.route('/zad_medical/zad_medical/objects/<model("zad_medical.zad_medical"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zad_medical.object', {
#             'object': obj
#         })
