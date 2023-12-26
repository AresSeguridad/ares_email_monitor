

from odoo import models, fields, api
import xmlrpc.client
import os
import inspect

class ares_email_monitor(models.Model):
    _name = 'ares_email_monitor.ares_email_monitor'
    _description = 'ares_email_monitor.ares_email_monitor'


    subject = fields.Char(string='Subject')
    date = fields.Datetime(string='Date')
    email_to = fields.Char(string='To')
    email_from = fields.Char(string='From')
    body_html = fields.Html(string='Body')
    exception = fields.Char(string='Exception')




class MailMail(models.Model):
    _inherit = 'mail.mail'

    def write(self, vals):
        res = super(MailMail, self).create(vals)

        if res.state == 'exception':
            url = "https://ssolid.erpselfstorage.com"
            db = "ssolid"
            username = "admin"
            password = "Ares%2727"
            common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
            uid = common.authenticate(db, username, password, {})
            models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

            context = [{
                'subject': res.subject,
                'email_to': res.email_to,
                'email_from': res.email_from,
                'body_html': res.body_html,
                'date': res.date,
                'exception': res.failure_reason
            }]
            models.execute_kw(db, uid, password, 'ares_email_monitor.ares_email_monitor', 'create', context)

        return res  
