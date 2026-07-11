import requests
import pandas as pd
import time


BASE_URL = "https://api.btcturk.com"


def get_markets():

    print("BtcTurk market çekiliyor...")

    url = f"{BASE_URL}/api/v2/server/exchangeinfo"

    try:
        r = requests.get(url, timeout=15)

        print("Market cevap:", r.status_code)

        data = r.json()

        markets = []

        for item in data.get("data", {}).get("symbols", []):

            symbol = item.get("name")

            if symbol and symbol.endswith("TRY"):
                markets.append(symbol)


        print("Market sayısı:", len(markets))

        return markets


    except Exception as e:

        print("Market hatası:", e)

        return []




def get_ohlc(symbol, limit=100):

    print("Mum isteniyor:", symbol)

    url = f"{BASE_URL}/api/v2/ohlc"


    params = {
        "pairSymbol": symbol,
        "resolution": "15",
        "limit": limit
    }


    try:

        r = requests.get(
            url,
            params=params,
            timeout=5
        )


        print(
            symbol,
            "mum cevap:",
            r.status_code
        )


        data = r.json()


        candles = data.get("data", [])


        if not candles:

            print(
                symbol,
                "mum boş"
            )

            return pd.DataFrame()



        df = pd.DataFrame(candles)


        return df



    except requests.exceptions.Timeout:

        print(
            symbol,
            "TIMEOUT"
        )

        return pd.DataFrame()


    except Exception as e:

        print(
            symbol,
            "mum hata:",
            e
        )

        return pd.DataFrame()




def get_price(symbol):

    try:

        url = f"{BASE_URL}/api/v2/ticker"


        r = requests.get(
            url,
            params={
                "pairSymbol":symbol
            },
            timeout=5
        )


        data = r.json()


        return float(
            data["data"][0]["last"]
        )


    except Exception as e:

        print(
            "Fiyat hatası:",
            e
        )

        return None
