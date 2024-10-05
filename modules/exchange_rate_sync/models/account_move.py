from odoo import models, fields, api, _
from datetime import datetime, date, timedelta
import http.client

class AccountMove(models.Model):
    _inherit = "account.move"


    def _get_daily_rate(self, count):
        data_detail = ''
        headers = {
            'x-ibm-client-id': "bdc1fe35-f88c-42ee-b0e2-1c6d3881ad86",
            'accept': "application/json"
            }
        start_period = str(fields.Date.today()) 
        end_period   = str(fields.Date.today())
        if count > 0:
            start_period = str(fields.Date.today()+timedelta(days=2) - timedelta(days=count)) 
            end_period   = str(fields.Date.today()+timedelta(days=2) - timedelta(days=count))
            
        currency = self.currency_id.name
  
        conn = http.client.HTTPSConnection("apigw1.bot.or.th")
        conn.request("GET", "/bot/public/Stat-ExchangeRate/v2/DAILY_AVG_EXG_RATE/?start_period=" + start_period + "&end_period="+end_period + "&currency="+currency, headers=headers)
        
        res = conn.getresponse()
        data = res.read()

        data_detail = eval(data.decode("utf-8"))['result']['data']['data_detail']
        if not data_detail[0]['period']:
            count += 1
            data_detail = self._get_daily_rate(count)
        if data_detail:
            return data_detail
    
    def send_api_update_rate(self):
        data_detail = self._get_daily_rate(0)
        return {
            "name": _("Exchange Rate (BOT)"),
            "res_model": "wizard.exchange.rate.sync",
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "view_id": self.env.ref("exchange_rate_sync.wizard_exchange_rate_sync_view").id,
            "view_type": "form",
            "context": {
                "default_period": data_detail[0]['period'],
                "default_currency": data_detail[0]['currency_id'],
                "default_buying_sight": data_detail[0]['buying_sight'],
                "default_buying_transfer": data_detail[0]['buying_transfer'],
                "default_selling": data_detail[0]['selling'],
                },
            "target": "new",
        }

    
