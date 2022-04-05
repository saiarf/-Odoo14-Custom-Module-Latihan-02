# -*- coding: utf-8 -*-
# from odoo import http


# class ZippyBook(http.Controller):
#     @http.route('/zippy__book/zippy__book/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zippy__book/zippy__book/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('zippy__book.listing', {
#             'root': '/zippy__book/zippy__book',
#             'objects': http.request.env['zippy__book.zippy__book'].search([]),
#         })

#     @http.route('/zippy__book/zippy__book/objects/<model("zippy__book.zippy__book"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zippy__book.object', {
#             'object': obj
#         })
