from config import (
    BUY_SCORE,
    WATCH_SCORE
)


def analyze(data):

    score = 50
    reasons = []

    price = data["price"]

    rsi = data["rsi"]

    ema9 = data["ema9"]
    ema21 = data["ema21"]
    ema50 = data["ema50"]

    macd = data["macd"]
    macd_signal = data["macd_signal"]

    atr = data["atr"]

    volume_ratio = data["volume_ratio"]


    # RSI

    if 45 <= rsi <= 65:
        score += 15
        reasons.append(
            "RSI GÜÇLÜ"
        )

    elif rsi > 70:
        score -= 10
        reasons.append(
            "RSI ŞİŞMİŞ"
        )


    # EMA trend

    if ema9 > ema21:
        score += 10
        reasons.append(
            "EMA YUKARI"
        )

    elif ema9 > ema50:
        score += 5
        reasons.append(
            "EMA YAKLAŞIYOR"
        )


    # MACD

    if macd > macd_signal:
        score += 15
        reasons.append(
            "MACD AL"
        )


    # Hacim

    if volume_ratio >= 2:
        score += 15
        reasons.append(
            "ÇOK GÜÇLÜ HACİM"
        )

    elif volume_ratio >= 1.3:
        score += 8
        reasons.append(
            "HACİM ARTIYOR"
        )


    # Puan sınırları

    score = max(
        0,
        min(
            score,
            100
        )
    )


    # Stop / hedef

    stop = price - (atr * 1.2)

    target1 = price + (atr * 3)

    target2 = price + (atr * 6)



    if score >= BUY_SCORE:

        signal = "🟢 BUY"

    elif score >= WATCH_SCORE:

        signal = "🟡 WATCH"

    else:

        signal = "🔴 SELL"



    return {

        "score": round(score),

        "signal": signal,

        "reasons": reasons,

        "price": price,

        "stop": round(stop, 4),

        "target1": round(target1, 4),

        "target2": round(target2, 4),

        "risk_reward": 2.5

    }
