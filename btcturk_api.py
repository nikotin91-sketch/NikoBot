import requests
import pandas as pd
import time


BASE_URL = "https://api.btcturk.com"


def get_markets():
    """
    BtcTurk market listesini alır.
    TRY çiftlerini döndürür.
    """

    url = f"{BASE_URL}/api/v2/server/exchangeinfo"

    try:
        r = requests.get(url, timeout=10)
        data = r.json()

        markets = []

        for item in data.get("data", []):
            name = item.get("name", "")

            if name.endswith("TRY"):
                markets.append(name)

        return markets

    except Exception as e:
        print("Market çekme hatası:", e)
        return []


def get_ohlc(symbol, limit=100):
    """
    Mum verisi çeker.
    """

    url = f"{BASE_URL}/api/v2/ohlc"

    params = {
        "symbol": symbol,
        "resolution": "15",
        "limit": limit
    }

    try:
        r = requests.get(url, params=params, timeout=10)
        data = r.json()

        candles = data.get("data", [])

        df = pd.DataFrame(
            candles,
            columns=[
                "time",
                "open",
                "high",
                "low",
                "close",
                "volume"
            ]
        )

        return df.astype(float)

    except Exception as e:
        print(symbol, "OHLC hata:", e)
        return pd.DataFrame()


def get_price(symbol):

    url = f"{BASE_URL}/api/v2/ticker"

    try:
        r = requests.get(
            url,
            params={"pairSymbol": symbol},
            timeout=10
        )

        data = r.json()

        return float(
            data["data"][0]["last"]
        )

    except Exception as e:
        print("Fiyat hatası:", e)
        return None



if __name__ == "__main__":

    coins = get_markets()

    print(
        "TRY market sayısı:",
        len(coins)
    )

    print(
        coins[:10]
    )
