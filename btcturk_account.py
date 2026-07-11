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

    try:

        secret_bytes = base64.b64decode(SECRET)

    except Exception:

        print("SECRET BASE64 değil")
        secret_bytes = SECRET.encode("utf-8")


    signature = hmac.new(
        secret_bytes,
        message.encode("utf-8"),
        hashlib.sha256
    ).digest()


    signature = base64.b64encode(
        signature
    ).decode("utf-8")


    headers = {

        "X-PCK": API_KEY,

        "X-Stamp": nonce,

        "X-Signature": signature,

        "Content-Type": "application/json"

    }


    return headers



def get_balance(asset="TRY"):


    url = (
        BASE_URL +
        "/api/v1/users/balances"
    )


    try:


        headers = create_headers()


        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )


        print(
            "BALANCE HTTP:",
            response.status_code
        )


        print(
            "BALANCE RAW:",
            response.text
        )


        if response.status_code != 200:

            return 0



        data = response.json()



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
