from pycoingecko import CoinGeckoAPI
from .tokens import currencies
import datetime

now = datetime.datetime.now()

class CoinGecko():
    def __init__(self):
        self.api = CoinGeckoAPI()
        # TODO: get currencies from database
        self.currencies = [c for c in currencies.values()]

    def get_currencies(self):
        response = self.api.get_price(
            ids=self.currencies,
            vs_currencies='eur',
            include_24hr_change=True,
            include_last_updated_at=True
        )

        print(response)
        # print(response['name'])
        # print(response['market_data']['current_price']['eur'], '€', sep='')
        # print(now.strftime(info['last_updated']))
    
    def get_values():
        pass
