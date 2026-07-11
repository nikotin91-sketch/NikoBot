import requests
import pandas as pd


BASE_URL = "https://api.btcturk.com"


HEADERS = {
    "User-Agent": "Mozilla/5.0"
}



def get_markets():

    url = f"{BASE_URL}/api/v2/server/exchangeinfo"


    print(
        "BtcTurk market isteği gönderiliyor..."
    )


    try:

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=(5, 15)
        )


        print(
            "Market HTTP:",
            response.status_code
        )


        print(
            "Market cevap uzunluğu:",
            len(response.text)
        )


        data = response.json()


        symbols = (
            data
            .get("data", {})
            .get("symbols", [])
        )


        markets = []


        for item in symbols:

            symbol = item.get("name")


            if symbol and symbol.endswith("TRY"):

                markets.append(symbol)



        print(
            "Bulunan TRY market:",
            len(markets)
        )


        return markets



    except requests.exceptions.Timeout:

        print(
            "Market isteği zaman aşımına uğradı"
        )

        return []


    except Exception as e:

        print(
            "Market hatası:",
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
            timeout=(5, 15)
        )


        data = response.json()


        candles = data.get(
            "data",
            []
        )


        if not candles:

            return pd.DataFrame()



        return pd.DataFrame(
            candles
        )



    except Exception as e:

        print(
            symbol,
            "OHLC hatası:",
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

            timeout=(5, 15)

        )


        data = response.json()


        return float(
            data["data"][0]["last"]
        )


    except Exception as e:


        print(
            "Fiyat hatası:",
            repr(e)
        )


        return None
