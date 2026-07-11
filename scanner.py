import time

from config import SCAN_INTERVAL

from btcturk_api import (
    get_markets,
    get_ohlc
)

from indicators import (
    add_indicators,
    get_latest_analysis
)

from ai_engine import analyze



def scan_market():

    markets = get_markets()

    print(
        "Taranan market:",
        len(markets)
    )

    signals = []


    for symbol in markets:

        try:

            df = get_ohlc(symbol)


            if df.empty:
                continue


            df = add_indicators(df)


            data = get_latest_analysis(df)


            if not data:
                continue


            result = analyze(data)


            result["symbol"] = symbol


            if result["score"] >= 70:

                signals.append(result)


                print(
                    symbol,
                    result["signal"],
                    result["score"]
                )


        except Exception as e:

            print(
                symbol,
                "hata:",
                e
            )


    signals.sort(
        key=lambda x: x["score"],
        reverse=True
    )


    return signals[:10]




def run():

    while True:

        print(
            "AI Scanner çalışıyor..."
        )


        results = scan_market()


        print(
            "En güçlü fırsatlar:"
        )


        for item in results:

            print(item)


        time.sleep(
            SCAN_INTERVAL
        )



if __name__ == "__main__":

    run()
