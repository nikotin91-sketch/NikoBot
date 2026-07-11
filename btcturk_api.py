import requests
import pandas as pd


BASE_URL = "https://api.btcturk.com"


def get_markets():

    url = f"{BASE_URL}/api/v2/server/exchangeinfo"

    try:
        response = requests.get(
            url,
            timeout=10
        )

        data = response.json()

        markets = []

        for item in data.get("data", {}).get("symbols", []):

            symbol = item.get("name")

            if symbol and symbol.endswith("TRY"):
                markets.append(symbol)

        return markets


    except Exception as e:

        print(
            "Market çekme hatası:",
            e
        )

        return []




def get_ohlc(symbol, limit=100):

    url = f"{BASE_URL}/api/v2/ohlc"

    params = {
        "pairSymbol": symbol,
        "resolution": "15",
        "limit": limit
    }


    try:

        response = requests.get(
            url,
            params=params,
            timeout=10
        )


        data = response.json()

        candles = data.get(
            "data",
            []
        )


        if not candles:
            return pd.DataFrame()



        df = pd.DataFrame(
            candles
        )


        return df



    except Exception as e:

        print(
            symbol,
            "mum hatası:",
            e
        )

        return pd.DataFrame()




def get_price(symbol):

    url = f"{BASE_URL}/api/v2/ticker"

    try:

        response = requests.get(
            url,
            params={
                "pairSymbol": symbol
            },
            timeout=10
        )


        data = response.json()


        return float(
            data["data"][0]["last"]
        )


    except Exception as e:

        print(
            "Fiyat hatası:",
            e
        )

        return None
