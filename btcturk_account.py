import os
import time
import base64
import hmac
import hashlib
import requests


API_KEY = os.getenv("BTCTURK_API_KEY","")
SECRET = os.getenv("BTCTURK_SECRET","")

BASE_URL = "https://api.btcturk.com"



def create_headers():

    stamp = str(
        int(time.time()*1000)
    )


    data = (
        API_KEY +
        stamp
    )


    secret = base64.b64decode(
        SECRET
    )


    signature = hmac.new(
        secret,
        data.encode("utf-8"),
        hashlib.sha256
    ).digest()


    return {

        "X-PCK": API_KEY,

        "X-Stamp": stamp,

        "X-Signature": base64.b64encode(
            signature
        ).decode(),

        "Content-Type":
            "application/json"

    }




def get_balance(asset="TRY"):


    try:


        url = (
            BASE_URL +
            "/api/v1/users/balances"
        )


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
            "BALANCE HEADER:",
            r.headers
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
            "BALANCE ERROR:",
            e
        )


        return 0
