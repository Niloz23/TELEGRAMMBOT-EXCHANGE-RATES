
import json
import requests
from config import keys

class APIException(Exception):
    pass

class CryptoConvector:
    @staticmethod
    def get_price( quote: str, base: str, amount: int):


        if quote == base:
            raise APIException(f'невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'не удалось обработать валюту - {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'не удалось обработать валюту - {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'не удалось обработать количество : {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        return total_base


