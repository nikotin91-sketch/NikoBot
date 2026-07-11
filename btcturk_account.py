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


    print(
        "API KEY VAR:",
        bool(API_KEY),
        flush=True
    )

    print(
        "SECRET VAR:",
        bool(SECRET),
        flush=True
    )


    message = (
        API_KEY +
        nonce
    )


    try:

        secret_bytes = base64.b64decode(
            SECRET
        )

    except Exception:

        secret_bytes = SECRET.encode(
            "utf-8"
        )


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


    print(
        "NONCE:",
        nonce,
        flush=True
    )


    return headers




def get_balance(asset="TRY"):


    url = (
        BASE_URL +
        "/api/v1/users/balances"
    )


    try:


        response = requests.get(

            url,

            headers=create_headers(),

            timeout=15

        )


        print(
            "BALANCE HTTP:",
            response.status_code,
            flush=True
        )


        print(
            "BALANCE RAW:",
            response.text,
            flush=True
        )



        if response.status_code != 200:

            return 0



        if not response.text.strip():

            return 0



        data = response.json()



        balances = data.get(
            "data",
            []
        )



        for item in balances:


            if item.get("asset") == asset:


                balance = float(

                    item.get(
                        "available",
                        0
                    )

                )


                print(
                    "BAKIYE:",
                    balance,
                    asset,
                    flush=True
                )


                return balance



        return 0



    except Exception as e:


        print(
            "BALANCE HATA:",
            e,
            flush=True
        )


        return 0
