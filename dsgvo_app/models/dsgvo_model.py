# -*- coding: utf-8 -*-

from odoo import api, fields, models, osv
from datetime import datetime
import time
#from dateutil.relativedelta import relativedelta
#from dateutil import*



class DsgvoTask(models.Model):
    _name = 'dsgvo.task'
    name = fields.Char('Titel',readonly=True)
    is_done = fields.Boolean('Task abgeschlossen?')
    active = fields.Boolean('Active?', default=True)
    user_id = fields.Many2one('res.users', 'Zuständig')
    date_deadline = fields.Date('Deadline')
    date_start = fields.Datetime('Projekt Start')
    date_end = fields.Datetime('Projekt Ende')
    m_currency_id = fields.Many2one('res.currency','Währung')
    _inherit = ['mail.thread']
    beschreibung = fields.Text('Beschreibung',readonly=True)
    zielsetzung = fields.Text('Zielsetzung', readonly=True)
    taetigkeiten = fields.Text('Tätigkeiten', readonly=True)
    aufwand_intern = fields.Float('Aufwand intern in Std.')
    aufwand_extern = fields.Float('Aufwand extern in Std.')
    kosten_intern = fields.Float('Gesamtkosten intern',readonly=True)
    kosten_extern = fields.Float('Gesamtkosten extern',readonly=True)
    in_notes = fields.Text()
    priority = fields.Selection([('0','Sehr gering'),('1','Niedrig'),('2','Normal'),('3','Hoch'),('4','Sehr hoch')])
    erw = fields.Text('Erwägungsgrund',readonly=True)
    links = fields.Html('Erwägungsgrund(Ewg)',readonly=True)
    links_art = fields.Html('Artikel DSGVO',readonly=True)
    ref = fields.Html('Referenzen',readonly=True)
    status = fields.Selection([('0','offen'),('1','begonnen'),('2','erledigt'),('3','nicht relevant')],track_visibility='always')
    status2 = fields.Selection([('0','offen'),('1','begonnen'),('2','erledigt'),('3','nicht relevant')],track_visibility='always')
    bearbeiteter_task = fields.Selection([('0','Task 1'),('1','Task 2'),('2','Task 3')],track_visibility='always')
    bearbeiteter_task2 = fields.Selection([('0','Task 1'),('1','Task 2'),('2','Task 3'),('3','Task 4'),('4','Task 5'),('5','Task 6'),('6','Task 7'),('7','Task 8')
                                  ,('8','Task 9'),('9','Task 10'),('10','Task 11'),('11','Task 12'),('12','Task 13'),('13','Task 14'),('14','Task 15'),('15','Task 16'),('16','Task 17')
                                  ,('17','Task 18')],track_visibility='always')
    anmerk = fields.Char('Anmerkung',track_visibility='always')
    anmerk2 = fields.Char('Anmerkung 2',track_visibility='always')
    duration = fields.Char("Durchlaufszeit",readonly=True)
    ksatz_intern = fields.Float("Kostensatz intern")
    ksatz_extern = fields.Float("Kostensatz extern")
    haftungsausschluss = fields.Char('Haftungsausschluss',readonly=True)
    platzhalter = fields.Char(readonly=True)
    
#    datenkatrw = ['Ordnungsnummer','Name bzw. Bezeichnung','Anrede/Geschlecht','Anschrift']
    
#    datenkatrw = fields.Selection([('0','Ordnungsnummer','1','Name')])

#    datenkatrw = fields.Char('Anschrift')
    
    @api.one
    def do_toggle_done(self):
        self.is_done = not self.is_done
        
        
        fmt = '%Y-%m-%d %H:%M:%S'
        dt1 = datetime.strptime(self.date_start,fmt)
        dt2 = datetime.strptime(self.date_end,fmt)
        diff = dt2 - dt1
        hours = diff.seconds / 3600
        days = diff.days
#        minutes = diff.seconds / 60
        
        
        self.write({'duration':"%02d Tage : %02d Stunden" % (days, hours)})
        return True




   
########Calculation of Duration########    

            
    @api.one
#    @api.depends('date_start','date_end')
    def calc_duration(self):
        
        fmt = '%Y-%m-%d %H:%M:%S'
        dt1 = datetime.strptime(self.date_start,fmt)
        dt2 = datetime.strptime(self.date_end,fmt)
        diff = dt2 - dt1
        hours = diff.seconds / 3600
        days = diff.days
#        minutes = diff.seconds / 60
        
        
        self.write({'duration':"%02d Tage : %02d Stunden" % (days, hours)})

        return True



########Calculation of Costs########


    @api.one
    def calc_cost(self):
    
        cost_intern = (self.ksatz_intern * self.aufwand_intern)
        cost_extern = (self.ksatz_extern * self.aufwand_extern)
        self.write({'kosten_intern':"%02f" % (cost_intern)})
        self.write({'kosten_extern':"%02f" % (cost_extern)})
        return True


















     
