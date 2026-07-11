import time

from config import SCAN_INTERVAL

from btcturk_api import (
    get_markets,
    get_ohlc,
    get_price
)

from database import (
    can_send_signal
)

from indicators import (
    add_indicators,
    get_latest_analysis
)

from ai_engine import analyze


def scan_market():

    print("PİYASA TARAMASI BAŞLIYOR")


    markets = get_markets()


    print(
        "Taranan market:",
        len(markets)
    )


    signals = []


    for symbol in markets:


        try:


            print(
                "OHLC BAŞLADI:",
                symbol
            )


            df = get_ohlc(symbol)


            if df is None:
                continue


            if df.empty:
                continue



            required_columns = [
                "open",
                "high",
                "low",
                "close"
            ]



            if not all(
                col in df.columns
                for col in required_columns
            ):

                print(
                    symbol,
                    "eksik kolon"
                )

                continue



            for col in required_columns:

                df[col] = df[col].astype(float)



            if len(df) < 60:


                print(
                    symbol,
                    "yetersiz mum:",
                    len(df)
                )

                continue



            df = add_indicators(df)



            data = get_latest_analysis(df)



            if not data:

                continue



            live_price = get_price(symbol)



            if live_price is not None:

                data["price"] = live_price



            result = analyze(data)



            if not result:

                continue



            result["symbol"] = symbol



            score = result.get(
                "score",
                0
            )


            price = result.get(
                "price",
                0
            )



            print(
                symbol,
                "SKOR:",
                score,
                "FİYAT:",
                price
            )



            if score >= 70:


                signal_type = result.get(
                    "signal",
                    "UNKNOWN"
                )


                if can_send_signal(
                    symbol,
                    signal_type,
                    300
                ):


                    signals.append(
                        result
                    )


                    print(
                        "SİNYAL:",
                        symbol,
                        signal_type,
                        score
                    )


                else:


                    print(
                        symbol,
                        "tekrar sinyal engellendi"
                    )



        except Exception as e:


            print(
                symbol,
                "hata:",
                str(e)
            )



    signals.sort(
        key=lambda x: x.get("score", 0),
        reverse=True
    )



    print(
        "TOPLAM SİNYAL:",
        len(signals)
    )



    return signals[:10]




def run():


    while True:


        try:


            results = scan_market()



            print(
                "GÜÇLÜ FIRSATLAR:"
            )



            for item in results:

                print(item)



        except Exception as e:


            print(
                "ANA HATA:",
                e
            )



        time.sleep(
            SCAN_INTERVAL
        )



if __name__ == "__main__":

    run()
