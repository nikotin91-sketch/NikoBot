import pandas as pd
import ta


def add_indicators(df):

    try:

        # BtcTurk kolonlarını düzenle
        df = df.copy()


        for col in [
            "open",
            "high",
            "low",
            "close",
            "volume"
        ]:

            if col in df.columns:

                df[col] = pd.to_numeric(
                    df[col],
                    errors="coerce"
                )


        df = df.dropna()


        if len(df) < 50:

            return pd.DataFrame()



        df["rsi"] = ta.momentum.RSIIndicator(
            df["close"],
            window=14
        ).rsi()



        df["ema9"] = ta.trend.EMAIndicator(
            df["close"],
            window=9
        ).ema_indicator()



        df["ema21"] = ta.trend.EMAIndicator(
            df["close"],
            window=21
        ).ema_indicator()



        macd = ta.trend.MACD(
            df["close"]
        )


        df["macd"] = macd.macd()

        df["macd_signal"] = macd.macd_signal()



        df = df.dropna()


        return df



    except Exception as e:

        print(
            "INDICATOR HATA:",
            e,
            flush=True
        )

        return pd.DataFrame()




def get_latest_analysis(df):

    try:

        if df.empty:
            return None


        last = df.iloc[-1]


        return {

            "price": float(last["close"]),

            "rsi": float(last["rsi"]),

            "ema9": float(last["ema9"]),

            "ema21": float(last["ema21"]),

            "macd": float(last["macd"]),

            "macd_signal": float(last["macd_signal"])

        }


    except Exception as e:

        print(
            "ANALYSIS HATA:",
            e,
            flush=True
        )

        return None
