# -*- coding: utf-8 -*-

from odoo import api, fields, models, osv

class empfaengerkategorien(models.Model):
    _name = 'dsgvo.empfaengerkategorien'
    name = fields.Char('Empfängerkategorien')
    