import os
import time
import hmac
import hashlib
import requests


API_KEY = os.getenv(
    "BTCTURK_API_KEY",
    ""
)

SECRET = os.getenv(
    "BTCTURK_SECRET",
    ""
)


BASE_URL = "https://api.btcturk.com"



def create_signature():

    nonce = str(
        int(time.time() * 1000)
    )

    message = (
        API_KEY +
        nonce
    )

    signature = hmac.new(
        base64.b64decode(SECRET),
        message.encode(),
        hashlib.sha256
    ).digest()


    return nonce, signature.hex()




def place_order(
    symbol,
    side,
    quantity,
    price
):

    print(
        "Emir hazırlanıyor:",
        symbol,
        side,
        quantity,
        price
    )


    # Gerçek emir bağlantısı
    # Test sonrası aktif edilecek


    return {
        "status": "prepared",
        "symbol": symbol,
        "side": side
    }
