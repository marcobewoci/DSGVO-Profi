# -*- coding: utf-8 -*-

from odoo import api, fields, models, osv

class verarbeitungstaetigkeiten(models.Model):
    _name = 'dsgvo.verarbeitungstaetigkeiten'
    name = fields.Char('Verarbeitungstätigkeiten')
    