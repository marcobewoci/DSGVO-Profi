# -*- coding: utf-8 -*-

from odoo import api, fields, models, osv



class verarbeitungsverzeichnis(models.Model):
    _name = 'ver.verzeichnis'
    # die Vererbung von dsgvo.task wird hier laut W.Pichler nicht benötigt => Felder werden doppelt angelegt
    _inherit = ['dsgvo.task']
    name = fields.Char('Verarbeitungsverzeichnis Titel', readonly=False)
    # required=True, copy=False, readonly=True, states={'draft': [('readonly', False)]}, index=True, default=lambda self: _('New'))
    niederl = fields.Boolean('Hauptniederlassung (ja/nein)')
    verantwortlich = fields.Many2one('res.users','Verantwortlich')
    street = fields.Char('Straße')
    postleitzahl = fields.Char('Postleitzahl')
    ort = fields.Char('Ort')
    telefon = fields.Char('Telefon')
    email = fields.Char('E-Mail')
    url = fields.Char('Webseite')

    verantwortlich2 = fields.Many2one('res.users','Verantwortlich')
    street2 = fields.Char('Straße')
    postleitzahl2 = fields.Char('Postleitzahl')
    ort2 = fields.Char('Ort')
    telefon2 = fields.Char('Telefon')
    email2 = fields.Char('E-Mail')

    verantwortlich3 = fields.Many2one('res.users','Verantwortlich')
    street3 = fields.Char('Straße')
    postleitzahl3 = fields.Char('Postleitzahl')
    ort3 = fields.Char('Ort')
    telefon3 = fields.Char('Telefon')
    email3 = fields.Char('E-Mail')

    titel = fields.Char('Titel')
    anrede = fields.Char('Anrede')
    dsb = fields.Char('Name, Vorname')
    street4 = fields.Char('Straße')
    postleitzahl4 = fields.Char('Postleitzahl')
    ort4 = fields.Char('Ort')
    telefon4 = fields.Char('Telefon')
    email4 = fields.Char('E-Mail')

    datum1 = fields.Date('Datum der Anlegung: ')
    datum2 = fields.Date('Datum der letzten Änderung: ')
    abteilung = fields.Char('Fachabteilung')
    ansprechpartner = fields.Char('Ansprechpartner')
    telefon5 = fields.Char('Telefon')
    email5 = fields.Char('E-Mail')


    verab_taetigkeiten = fields.Many2many('dsgvo.verarbeitungstaetigkeiten', string="Verarbeitungstätigkeiten")
    verab_zwecke = fields.Many2many('dsgvo.verarbeitungszwecke', string="Verarbeitungszwecke")
    kat_betroffenerpersonen = fields.Selection([('0','Beschäftigte'),('1','Interessenten'),('2','Lieferanten'),('3','Kunden'),('4','Patienten'),('5','Sonstige')])
    daten_kategorien = fields.Selection([('0','Name'),('1','Adresse'),('2','Geschlecht'),('3','Geburtsdatum'),('4','SVNR'),('5','Status')])
    kat_peroffengelegt = fields.Boolean('intern: ')
    peroffeng_i = fields.Char('Abteilung/Funktion')
    kat_peroffengelegt2 = fields.Boolean('extern: ')
    peroffeng_e = fields.Char('Empfängerkategorie')
    daten_ueb = fields.Boolean('Datenübermittlung findet nicht statt und ist auch nicht geplant')
    daten_ueb2 = fields.Boolean('Datenübermittlung findet wie folgt statt: ')
    daten_ueb3 = fields.Char('Drittland, Name: ')
    daten_ueb4 = fields.Char('internationale Organisation, Bezeichnung: ')
    daten_ueb5 = fields.Selection([('0','Mahnwesen'),('1','Gehaltsüberweisung'),('2','Sicherheit'),('3','Kundenbetreuung')])


    empfaengerkategorien = fields.Many2many('dsgvo.empfaengerkategorien',string="Nennung der konkreten Datenempfänger")
    gara_doku = fields.Text('Dokumentation geeigneter Garantien')
    doku_toms = fields.Text('Dokumentation der technischen und organisatorischen Maßnahmen')
    doku_loeschfristen = fields.Text('Dokumentation der Löschfristen')
    space = fields.Char('', readonly=True)
#    daten_rw = fields.Many2many('dsgvo.task')
    datenarten = fields.Many2many('dsgvo.datenarten', string="Datenkategorien")
    personengruppen = fields.Many2many('dsgvo.personengruppen',string="Personengruppen")
    empfaengerkreis = fields.Many2many('dsgvo.empfaengerkreis',string="Empfängerkategorien")


    # Button um Verarbeitungsverzeichnis zu drucken


    @api.multi
    def create_verarbeitungsverzeichnis(self):
        return self.env.ref('dsgvo_app.report_verarbeitungsverzeichnis').report_action(self, data=data)
       
        #return self.env.ref('dsgvo_app.report_verarbeitungsverzeichnis').get_action(self)