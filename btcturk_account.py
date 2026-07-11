import os
import time
import base64
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



def create_headers():

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


    return {

        "X-PCK": API_KEY,

        "X-Stamp": nonce,

        "X-Signature": base64.b64encode(
            signature
        ).decode()

    }




def get_balance(asset="TRY"):

    url = (
        BASE_URL +
        "/api/v1/users/balances"
    )


    try:

        response = requests.get(
            url,
            headers=create_headers(),
            timeout=10
        )


        data = response.json()


        for item in data.get("data", []):

            if item.get("asset") == asset:

                return float(
                    item.get("available", 0)
                )


        return 0


    except Exception as e:

        print(
            "Bakiye hatası:",
            e
        )

        return 0
