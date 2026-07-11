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

        r = requests.get(
            f"{BASE_URL}/api/v2/ohlc",
            params={
                "pairSymbol": symbol,
                "resolution": "15",
                "limit": limit
            },
            timeout=10
        )

        print("OHLC DURUM:", symbol, r.status_code, flush=True)

        if r.status_code != 200:
            return pd.DataFrame()

        candles = r.json().get("data", [])

        if not candles:
            return pd.DataFrame()

        df = pd.DataFrame(candles)

        rename = {
            "o": "open",
            "h": "high",
            "l": "low",
            "c": "close",
            "v": "volume"
        }

        df.rename(columns=rename, inplace=True)

        required = ["open", "high", "low", "close", "volume"]

        for col in required:
            if col not in df.columns:
                return pd.DataFrame()

            df[col] = pd.to_numeric(df[col], errors="coerce")

        df.dropna(inplace=True)
        df.reset_index(drop=True, inplace=True)

        print(
            f"{symbol} SON FİYAT: {df.iloc[-1]['close']}",
            flush=True
        )

        return df

    except Exception as e:

        print("OHLC HATA:", symbol, e, flush=True)

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

        data = r.json()["data"][0]

        return float(data["last"])

    except Exception as e:

        print("PRICE HATA:", e, flush=True)

        return None
