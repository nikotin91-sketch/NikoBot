import requests
import pandas as pd

BASE_URL = "https://api.btcturk.com"


def get_markets():

    print("BtcTurk market çekiliyor...", flush=True)

    try:

        r = requests.get(
            f"{BASE_URL}/api/v2/server/exchangeinfo",
            timeout=10
        )

        print("Market cevap:", r.status_code, flush=True)

        data = r.json()

        markets = []

        for item in data["data"]["symbols"]:

            name = item.get("name")

            if name and name.endswith("TRY"):
                markets.append(name)

        print("Market sayısı:", len(markets), flush=True)

        return markets

    except Exception as e:

        print("MARKET HATA:", e, flush=True)

        return []


def get_ohlc(symbol, limit=100):

    print("OHLC BAŞLADI:", symbol, flush=True)

    try:

        url = f"{BASE_URL}/api/v2/ohlc"

        params = {
            "pairSymbol": symbol,
            "resolution": "15",
            "limit": limit
        }

        print("İSTEK ATILIYOR:", symbol, flush=True)

        r = requests.get(
            url,
            params=params,
            timeout=5
        )

        print(
            "OHLC DURUM:",
            symbol,
            r.status_code,
            flush=True
        )

        data = r.json()

        candles = data.get("data")

        if not candles:

            print(
                "VERİ YOK:",
                symbol,
                flush=True
            )

            return pd.DataFrame()

        df = pd.DataFrame(candles)

        print(
            "MUM TAMAM:",
            symbol,
            len(df),
            flush=True
        )

        return df

    except Exception as e:

        print(
            "OHLC HATA:",
            symbol,
            e,
            flush=True
        )

        return pd.DataFrame()


def get_price(symbol):

    try:

        r = requests.get(
            f"{BASE_URL}/api/v2/ticker",
            params={
                "pairSymbol": symbol
            },
            timeout=5
        )

        data = r.json()

        return float(
            data["data"][0]["last"]
        )

    except Exception as e:

        print(
            "PRICE HATA:",
            e,
            flush=True
        )

        return None
