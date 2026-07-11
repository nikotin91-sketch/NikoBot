import pandas as pd
import ta



def add_indicators(df):

    try:

        df = df.copy()


        # Sayısala çevir

        cols = [
            "open",
            "high",
            "low",
            "close",
            "volume"
        ]


        for col in cols:

            if col in df.columns:

                df[col] = pd.to_numeric(
                    df[col],
                    errors="coerce"
                )



        df = df.dropna()



        # EMA50 için yeterli veri

        if len(df) < 60:

            return pd.DataFrame()



        # RSI

        df["rsi"] = ta.momentum.RSIIndicator(
            close=df["close"],
            window=14
        ).rsi()



        # EMA

        df["ema9"] = ta.trend.EMAIndicator(
            close=df["close"],
            window=9
        ).ema_indicator()



        df["ema21"] = ta.trend.EMAIndicator(
            close=df["close"],
            window=21
        ).ema_indicator()



        df["ema50"] = ta.trend.EMAIndicator(
            close=df["close"],
            window=50
        ).ema_indicator()



        # MACD

        macd = ta.trend.MACD(
            close=df["close"]
        )


        df["macd"] = macd.macd()

        df["macd_signal"] = macd.macd_signal()

        df["macd_hist"] = macd.macd_diff()



        # Son boşları temizle

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

            "ema50": float(last["ema50"]),

            "macd": float(last["macd"]),

            "macd_signal": float(last["macd_signal"]),

            "macd_hist": float(last["macd_hist"])

        }



    except Exception as e:

        print(
            "ANALYSIS HATA:",
            e,
            flush=True
        )

        return None
