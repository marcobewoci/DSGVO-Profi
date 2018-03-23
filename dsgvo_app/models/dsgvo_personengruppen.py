# -*- coding: utf-8 -*-

from odoo import api, fields, models, osv

class personengruppen(models.Model):
    _name = 'dsgvo.personengruppen'
    name = fields.Char('Personengruppen')
    