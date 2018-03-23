# -*- coding: utf-8 -*-
{

    'name': 'DSGVO Profi',
    'summary': 'Meistern Sie die Datenschutz-Grundverordnung.',
    'website': 'https://www.bewoci.eu',
    'author': 'bewoci GmbH',
    'version': '1.0',
    'category':'Project',
    'license': 'AGPL-3',
    'price': 249.00,
    'currency':'EUR',
    'depends': ['mail'],
    'installable': True, 
    'application': True,
    'data': [
    'views/dsgvo_view.xml',
    'views/verarbeitungsverzeichnis_view.xml',
    'views/default_data_view.xml',
    'views/dsgvo_personengruppen_view.xml',
    'views/dsgvo_empfaengerkreise_view.xml',
    'views/dsgvo_empfaengerkategorien_view.xml',
    'views/dsgvo_verarbeitungstaetigkeiten_view.xml',
    'views/dsgvo_verarbeitungszwecke_view.xml',
    'security/ir.model.access.csv',
    'reports/report_verarbeitungsverzeichnis.xml',
    'security2/ir.model.access.csv',
    'security3/ir.model.access.csv',
    'security4/ir.model.access.csv',
    'security5/ir.model.access.csv',
    'security6/ir.model.access.csv',
    'security7/ir.model.access.csv',
    'security8/ir.model.access.csv',
    
],

}