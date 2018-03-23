# -*- coding: utf-8 -*-

from odoo import api, fields, models, osv

class verarbeitungszwecke(models.Model):
    _name = 'dsgvo.verarbeitungszwecke'
    name = fields.Char('Verarbeitungszwecke')
    