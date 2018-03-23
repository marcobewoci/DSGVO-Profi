# -*- coding: utf-8 -*-

from odoo import api, fields, models, osv

class empfaengerkreise(models.Model):
    _name = 'dsgvo.empfaengerkreis'
    name = fields.Char('Empfängerkategorien')
    