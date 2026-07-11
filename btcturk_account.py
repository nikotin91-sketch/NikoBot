import os
import time
import base64
import hmac
import hashlib
import requests


API_KEY = os.getenv("BTCTURK_API_KEY")
SECRET = os.getenv("BTCTURK_SECRET")

BASE_URL = "https://api.btcturk.com"


# açık pozisyon hafızası
OPEN_POSITIONS = {}



def create_headers():

    if not API_KEY or not SECRET:
        print("API KEY veya SECRET yok")
        return {}


    nonce = str(int(time.time() * 1000))


    message = API_KEY + nonce


    try:

        secret_bytes = base64.b64decode(
            SECRET
        )

    except Exception:

        print("SECRET BASE64 HATALI")
        return {}



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



        if r.status_code != 200:

            print(
                "BALANCE ERROR:",
                r.text
            )

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






def calculate_trade(balance, price):


    # bakiyenin %10'u

    amount = balance * 0.10


    quantity = amount / price



    return round(
        quantity,
        8
    )






def create_position(symbol, price, score):


    stop = price * 0.97

    target = price * 1.06



    OPEN_POSITIONS[symbol] = {


        "buy_price": price,

        "stop": stop,

        "target": target,

        "score": score


    }



    print(
        "POZİSYON AÇILDI:",
        OPEN_POSITIONS[symbol]
    )








def check_position(symbol, price):


    if symbol not in OPEN_POSITIONS:

        return None



    pos = OPEN_POSITIONS[symbol]



    if price <= pos["stop"]:


        print(
            "STOP:",
            symbol
        )

        del OPEN_POSITIONS[symbol]

        return "STOP"



    if price >= pos["target"]:


        print(
            "HEDEF:",
            symbol
        )

        del OPEN_POSITIONS[symbol]

        return "TARGET"



    return "HOLD"







def signal_message(symbol, score, price):


    if score >= 90:


        return f"""

🟢 BUY SİNYALİ

Coin: {symbol}

Skor: {score}

Fiyat: {price}

Stop: %{3}

Hedef: %{6}

"""



    elif score >= 75:


        return f"""

🟡 WATCH

Coin: {symbol}

Skor: {score}

Fiyat: {price}

"""


    return None import os
import time
import base64
import hmac
import hashlib
import requests


API_KEY = os.getenv("BTCTURK_API_KEY")
SECRET = os.getenv("BTCTURK_SECRET")

BASE_URL = "https://api.btcturk.com"


# açık pozisyon hafızası
OPEN_POSITIONS = {}



def create_headers():

    if not API_KEY or not SECRET:
        print("API KEY veya SECRET yok")
        return {}


    nonce = str(int(time.time() * 1000))


    message = API_KEY + nonce


    try:

        secret_bytes = base64.b64decode(
            SECRET
        )

    except Exception:

        print("SECRET BASE64 HATALI")
        return {}



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



        if r.status_code != 200:

            print(
                "BALANCE ERROR:",
                r.text
            )

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






def calculate_trade(balance, price):


    # bakiyenin %10'u

    amount = balance * 0.10


    quantity = amount / price



    return round(
        quantity,
        8
    )






def create_position(symbol, price, score):


    stop = price * 0.97

    target = price * 1.06



    OPEN_POSITIONS[symbol] = {


        "buy_price": price,

        "stop": stop,

        "target": target,

        "score": score


    }



    print(
        "POZİSYON AÇILDI:",
        OPEN_POSITIONS[symbol]
    )








def check_position(symbol, price):


    if symbol not in OPEN_POSITIONS:

        return None



    pos = OPEN_POSITIONS[symbol]



    if price <= pos["stop"]:


        print(
            "STOP:",
            symbol
        )

        del OPEN_POSITIONS[symbol]

        return "STOP"



    if price >= pos["target"]:


        print(
            "HEDEF:",
            symbol
        )

        del OPEN_POSITIONS[symbol]

        return "TARGET"



    return "HOLD"







def signal_message(symbol, score, price):


    if score >= 90:


        return f"""

🟢 BUY SİNYALİ

Coin: {symbol}

Skor: {score}

Fiyat: {price}

Stop: %{3}

Hedef: %{6}

"""



    elif score >= 75:


        return f"""

🟡 WATCH

Coin: {symbol}

Skor: {score}

Fiyat: {price}

"""


    return None
