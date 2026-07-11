import os
import time
import hmac
import hashlib
import base64
import requests


API_KEY = os.getenv("BTCTURK_API_KEY", "")
SECRET = os.getenv("BTCTURK_SECRET", "")

BASE_URL = "https://api.btcturk.com"


def create_signature():

    nonce = str(int(time.time() * 1000))

    message = API_KEY + nonce

    signature = hmac.new(
        base64.b64decode(SECRET),
        message.encode("utf-8"),
        hashlib.sha256
    ).digest()

    return nonce, base64.b64encode(signature).decode("utf-8")


def create_headers():

    nonce, signature = create_signature()

    return {
        "X-PCK": API_KEY,
        "X-Stamp": nonce,
        "X-Signature": signature,
        "Content-Type": "application/json"
    }


def place_order(symbol, side, quantity, price):

    print(
        "Emir hazırlanıyor:",
        symbol,
        side,
        quantity,
        price,
        flush=True
    )

    # Şimdilik gerçek emir göndermiyor.
    # Gerçek emir kodunu eklediğinde create_headers() kullanılacak.

    return {
        "status": "prepared",
        "symbol": symbol,
        "side": side,
        "quantity": quantity,
        "price": price
    }
