# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, models, fields, _

class WizardExchangeRateSync(models.TransientModel):
    _name = 'wizard.exchange.rate.sync'
    _description = 'Wizard Exchange rate sync'

    
    currency = fields.Char('Currency')
    selling = fields.Float('Selling', digits=(16,4))
    buying_sight = fields.Float('Buying Bills', digits=(16,4))
    buying_transfer = fields.Float('Buying Transfer', digits=(16,4))
    period = fields.Char('Period')