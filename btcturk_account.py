import os
import time
import hmac
import hashlib
import requests


API_KEY = os.getenv("BTCTURK_API_KEY")
SECRET = os.getenv("BTCTURK_SECRET")

BASE_URL = "https://api.btcturk.com"


def create_headers():

    if not API_KEY or not SECRET:
        print("API KEY veya SECRET yok")
        return {}


    nonce = str(int(time.time() * 1000))

    message = API_KEY + nonce


    signature = hmac.new(
        SECRET.encode("utf-8"),
        message.encode("utf-8"),
        hashlib.sha256
    ).digest()


    import base64

    signature = base64.b64encode(
        signature
    ).decode("utf-8")


    headers = {

        "X-PCK": API_KEY,

        "X-Stamp": nonce,

        "X-Signature": signature,

        "Content-Type": "application/json"

    }


    print("NONCE:", nonce)

    return headers



def get_balance(asset="TRY"):


    url = BASE_URL + "/api/v1/users/balances"


    try:


        headers = create_headers()


        r = requests.get(
            url,
            headers=headers,
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


        balances = data.get(
            "data",
            []
        )


        for item in balances:


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
