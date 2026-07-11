import os
import time
import base64
import hmac
import hashlib
import requests


API_KEY = os.getenv("BTCTURK_API_KEY", "")
SECRET = os.getenv("BTCTURK_SECRET", "")

BASE_URL = "https://api.btcturk.com"


def create_headers():

    nonce = str(int(time.time() * 1000))

    message = API_KEY + nonce

    signature = hmac.new(
        base64.b64decode(SECRET),
        message.encode("utf-8"),
        hashlib.sha256
    ).digest()

    return {
        "X-PCK": API_KEY,
        "X-Stamp": nonce,
        "X-Signature": base64.b64encode(signature).decode("utf-8"),
        "Content-Type": "application/json"
    }


def get_balance(asset="TRY"):

    url = BASE_URL + "/api/v1/users/balances"

    try:

        response = requests.get(
            url,
            headers=create_headers(),
            timeout=15
        )

        print("BALANCE HTTP:", response.status_code)

        if response.status_code != 200:
            print("API CEVABI:")
            print(response.text)
            return 0

        if not response.text.strip():
            print("Boş cevap geldi.")
            return 0

        try:
            data = response.json()
        except Exception:
            print("JSON okunamadı:")
            print(response.text)
            return 0

        if "data" not in data:
            print(data)
            return 0

        for item in data["data"]:

            if item.get("asset") == asset:

                return float(
                    item.get("available", 0)
                )

        return 0

    except requests.exceptions.RequestException as e:
        print("Bağlantı hatası:", e)
        return 0

    except Exception as e:
        print("Bakiye hatası:", e)
        return 0
