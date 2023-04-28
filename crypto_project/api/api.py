import requests
from django.conf import settings

from .models import CryptoCurrency
from crypto_project.settings import COINMARKETCAP_API_KEY



def update_crypto_currencies():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": COINMARKETCAP_API_KEY
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    for crypto in data["data"]:
        symbol = crypto["symbol"]
        name = crypto["name"]
        current_price = crypto["quote"]["USD"]["price"]
        price_change_24h = crypto["quote"]["USD"]["percent_change_24h"]
        volume_24h = crypto["quote"]["USD"]["volume_24h"]

        CryptoCurrency.objects.update_or_create(
            symbol=symbol,
            defaults={
                'name': name,
                'current_price': round(current_price, 4),
                'price_change_24h': round(price_change_24h, 4),
                'volume_24h': round(volume_24h, 4)
            }
        )

