# -*- coding: utf-8 -*-
# from odoo import http


# class AresEmailMonitor(http.Controller):
#     @http.route('/ares_email_monitor/ares_email_monitor/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ares_email_monitor/ares_email_monitor/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ares_email_monitor.listing', {
#             'root': '/ares_email_monitor/ares_email_monitor',
#             'objects': http.request.env['ares_email_monitor.ares_email_monitor'].search([]),
#         })

#     @http.route('/ares_email_monitor/ares_email_monitor/objects/<model("ares_email_monitor.ares_email_monitor"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ares_email_monitor.object', {
#             'object': obj
#         })
