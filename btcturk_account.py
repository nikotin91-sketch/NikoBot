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

    if not API_KEY or not SECRET:
        print("API KEY veya SECRET yok")
        return {}

    nonce = str(int(time.time() * 1000))

    message = nonce + API_KEY

    try:

        signature = hmac.new(
            base64.b64decode(SECRET),
            message.encode("utf-8"),
            hashlib.sha256
        ).digest()

    except Exception as e:

        print("SIGNATURE HATA:", e)
        return {}


    signature = base64.b64encode(
        signature
    ).decode("utf-8")


    print("API KEY VAR:", bool(API_KEY))
    print("SECRET VAR:", bool(SECRET))

    print("KEY UZUNLUK:", len(API_KEY))
    print("SECRET UZUNLUK:", len(SECRET))

    print("KEY BAS:", API_KEY[:6])
    print("SECRET BAS:", SECRET[:6])

    print("NONCE:", nonce)


    return {

        "X-PCK": API_KEY,

        "X-Stamp": nonce,

        "X-Signature": signature,

        "Content-Type": "application/json"

    }



def get_balance(asset="TRY"):

    url = BASE_URL + "/api/v1/users/balances"


    try:

        r = requests.get(
            url,
            headers=create_headers(),
            timeout=10
        )


        print(
            "BALANCE STATUS:",
            r.status_code
        )


        print(
            "BALANCE TEXT:",
            r.text
        )


        if r.status_code != 200:
            return 0


        data = r.json()


        for item in data.get("data", []):

            if item.get("asset") == asset:

                return float(
                    item.get(
                        "available",
                        0
                    )
                )


        return 0


    except Exception as e:

        print(
            "BALANCE HATA:",
            e
        )

        return 0
