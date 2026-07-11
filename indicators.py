import pandas as pd
import ta


def add_indicators(df):

    if df.empty or len(df) < 50:
        return df


    # RSI
    df["rsi"] = ta.momentum.RSIIndicator(
        df["close"],
        window=14
    ).rsi()


    # EMA
    df["ema9"] = ta.trend.EMAIndicator(
        df["close"],
        window=9
    ).ema_indicator()

    df["ema21"] = ta.trend.EMAIndicator(
        df["close"],
        window=21
    ).ema_indicator()

    df["ema50"] = ta.trend.EMAIndicator(
        df["close"],
        window=50
    ).ema_indicator()


    # MACD

    macd = ta.trend.MACD(
        df["close"],
        window_fast=12,
        window_slow=26,
        window_sign=9
    )

    df["macd"] = macd.macd()
    df["macd_signal"] = macd.macd_signal()
    df["macd_hist"] = macd.macd_diff()


    # ATR

    atr = ta.volatility.AverageTrueRange(
        high=df["high"],
        low=df["low"],
        close=df["close"],
        window=14
    )

    df["atr"] = atr.average_true_range()


    # Hacim ortalaması

    df["volume_avg"] = (
        df["volume"]
        .rolling(20)
        .mean()
    )

    df["volume_ratio"] = (
        df["volume"] /
        df["volume_avg"]
    )


    return df



def get_latest_analysis(df):

    if df.empty:
        return {}


    last = df.iloc[-1]


    return {

        "price": float(last["close"]),

        "rsi": float(last["rsi"]),

        "ema9": float(last["ema9"]),
        "ema21": float(last["ema21"]),
        "ema50": float(last["ema50"]),

        "macd": float(last["macd"]),
        "macd_signal": float(last["macd_signal"]),

        "atr": float(last["atr"]),

        "volume_ratio":
            float(last["volume_ratio"])

    }
