# -*- coding: utf-8 -*-

from odoo import api, fields, models, osv

class verarbeitungsverzeichniszwei(models.Model):
    _name = 'dsgvo.datenarten'
    name = fields.Char('Datenkategorien')
    