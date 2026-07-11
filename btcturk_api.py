import requests
import pandas as pd


BASE_URL = "https://api.btcturk.com"


HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}



def get_markets():

    url = f"{BASE_URL}/api/v2/server/exchangeinfo"


    print("BtcTurk market çekiliyor...")


    try:

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=5
        )


        print(
            "Market cevap:",
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

            name = item.get("name")


            if name and name.endswith("TRY"):

                markets.append(name)


        print(
            "Market sayısı:",
            len(markets)
        )


        return markets



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


        print(
            "Mum isteniyor:",
            symbol
        )


        response = requests.get(

            url,

            params=params,

            headers=HEADERS,

            timeout=5

        )


        print(

            symbol,

            "OHLC cevap:",

            response.status_code

        )



        data = response.json()



        candles = data.get(
            "data",
            []
        )



        if not candles:


            print(
                symbol,
                "mum bulunamadı"
            )


            return pd.DataFrame()



        df = pd.DataFrame(
            candles
        )



        print(

            symbol,

            "mum hazır:",

            len(df)

        )



        return df



    except Exception as e:


        print(

            symbol,

            "OHLC hata:",

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



        price = float(

            data["data"][0]["last"]

        )


        return price



    except Exception as e:


        print(

            symbol,

            "fiyat hata:",

            repr(e)

        )


        return None
