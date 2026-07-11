import requests
import pandas as pd


BASE_URL = "https://api.btcturk.com"


HEADERS = {
    "User-Agent": "Mozilla/5.0"
}



def get_markets():

    url = f"{BASE_URL}/api/v2/server/exchangeinfo"


    print(
        "BtcTurk bağlantı testi başladı"
    )


    try:

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=5
        )


        print(
            "BtcTurk cevap:",
            response.status_code
        )


        data = response.json()


        symbols = (
            data
            .get("data", {})
            .get("symbols", [])
        )


        markets = []


        for item in symbols:


            name = item.get(
                "name"
            )


            if name and name.endswith(
                "TRY"
            ):

                markets.append(
                    name
                )


        print(
            "Market sayısı:",
            len(markets)
        )


        return markets



    except Exception as e:


        print(
            "BTC API HATA:",
            repr(e)
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

            headers=HEADERS,

            timeout=5

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
            "OHLC HATA:",
            repr(e)
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

            headers=HEADERS,

            timeout=5

        )


        data = response.json()



        return float(
            data["data"][0]["last"]
        )



    except Exception as e:


        print(
            "Fiyat alma hatası:",
            repr(e)
        )


        return None
