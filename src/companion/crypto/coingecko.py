from pycoingecko import CoinGeckoAPI
from .tokens import currencies

import datetime
from copy import deepcopy

now = datetime.datetime.now()

class CoinGecko():
    def __init__(self):
        self.api = CoinGeckoAPI()
        # TODO: get currencies from database
        self.currencies = [c for c in currencies.values()]

    def get_currencies(self):
        ids = [c['id'] for c in self.currencies]
        response = self.api.get_price(
            ids,
            vs_currencies='eur',
            include_24hr_change=True,
            include_last_updated_at=True
        )

        currencies = []
        for currency in self.currencies:
            c = deepcopy(currency)
            c['price'] = response[c['id']]['eur']
            c['24h_change'] = response[c['id']]['eur_24h_change']
            currencies += [c]
        return currencies
    
    def get_values():
        pass
