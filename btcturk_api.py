import requests
import pandas as pd


BASE_URL = "https://api.btcturk.com"



def get_markets():

    url = f"{BASE_URL}/api/v2/server/exchangeinfo"


    print(
        "1 - BtcTurk isteği hazırlanıyor"
    )


    try:

        print(
            "2 - BtcTurk isteği gönderiliyor"
        )


        response = requests.get(

            url,

            headers={
                "User-Agent": "Mozilla/5.0",
                "Accept": "application/json"
            },

            timeout=5

        )


        print(
            "3 - BtcTurk cevap geldi:",
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
            "4 - Market bulundu:",
            len(markets)
        )


        return markets



    except requests.exceptions.Timeout:


        print(
            "BtcTurk zaman aşımı"
        )


        return []



    except Exception as e:


        print(
            "BtcTurk hata:",
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

            timeout=5

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
            "mum hatası:",
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

            timeout=5

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
