

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
    curremt_data_base = fields.Char(string="Current Data Base")
    current_record_id = fields.Integer(string="Current Record Id")




class MailMail(models.Model):
    _inherit = 'mail.mail'

    def write(self, vals):
        res = super(MailMail, self).write(vals)

        if self.state == 'exception':
            url = "https://ssolid.erpselfstorage.com"
            db = "ssolid"
            username = "admin"
            password = "Ares%2727"
            common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
            uid = common.authenticate(db, username, password, {})
            models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
            record_id = self.id
            db_error = self.env.cr.dbname

            context = [{
                'subject': self.subject,
                'email_to': self.email_to,
                'email_from': self.email_from,
                'body_html': self.body_html,
                'date': self.date,
                'exception': self.failure_reason,
                "curremt_data_base": db_error,
                "current_record_id": record_id,

            }]
            models.execute_kw(db, uid, password, 'ares_email_monitor.ares_email_monitor', 'create', context)

        return res
