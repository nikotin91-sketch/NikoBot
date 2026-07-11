import time

from config import SCAN_INTERVAL

from btcturk_api import (
    get_markets,
    get_ohlc
)

from btcturk_account import (
    get_balance
)

from indicators import (
    add_indicators,
    get_latest_analysis
)

from ai_engine import analyze

from risk_manager import (
    calculate_position_size
)

from trade_engine import (
    execute_buy
)



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



            # Veri kontrolü

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



            # String gelen fiyatları düzelt

            for col in required_columns:

                df[col] = df[col].astype(float)



            # En az 60 mum şartı

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
                score
            )



            # Güçlü sinyal

            if score >= 85:


                try:

                    balance = get_balance(
                        "TRY"
                    )


                    amount = calculate_position_size(
                        balance,
                        price
                    )


                    execute_buy(
                        symbol,
                        price,
                        amount
                    )


                    print(
                        "ALIM:",
                        symbol
                    )


                except Exception as e:

                    print(
                        "TRADE HATASI:",
                        e
                    )




            if score >= 70:

                signals.append(
                    result
                )


                print(
                    "SİNYAL:",
                    symbol,
                    result.get("signal"),
                    score
                )



        except Exception as e:


            print(
                symbol,
                "hata:",
                str(e)
            )



    signals.sort(
        key=lambda x:
        x.get("score",0),
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

                print(
                    item
                )


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
