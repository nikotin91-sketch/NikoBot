import os


# =========================
# TARAMA AYARLARI
# =========================

SCAN_INTERVAL = int(
    os.getenv(
        "SCAN_INTERVAL",
        60
    )
)


# Aynı coin aynı sinyal tekrar süresi
SIGNAL_COOLDOWN = int(
    os.getenv(
        "SIGNAL_COOLDOWN",
        300
    )
)



# =========================
# TELEGRAM AYARLARI
# =========================

TELEGRAM_TOKEN = os.getenv(
    "TELEGRAM_TOKEN"
)


TELEGRAM_CHAT_ID = os.getenv(
    "TELEGRAM_CHAT_ID"
)



# =========================
# BTCTURK API
# =========================

BTCTURK_API_KEY = os.getenv(
    "BTCTURK_API_KEY"
)


BTCTURK_SECRET = os.getenv(
    "BTCTURK_SECRET"
)



# =========================
# AI SİNYAL AYARLARI
# =========================

BUY_SCORE = int(
    os.getenv(
        "BUY_SCORE",
        85
    )
)


WATCH_SCORE = int(
    os.getenv(
        "WATCH_SCORE",
        70
    )
)



# =========================
# MUM AYARLARI
# =========================

MIN_CANDLES = int(
    os.getenv(
        "MIN_CANDLES",
        60
    )
)



# =========================
# RİSK AYARLARI
# =========================

STOP_ATR_MULTIPLIER = float(
    os.getenv(
        "STOP_ATR_MULTIPLIER",
        1.5
    )
)


TARGET1_RISK = float(
    os.getenv(
        "TARGET1_RISK",
        1.8
    )
)


TARGET2_RISK = float(
    os.getenv(
        "TARGET2_RISK",
        3.0
    )
)


RISK_REWARD = float(
    os.getenv(
        "RISK_REWARD",
        2.5
    )
)



# =========================
# TRADE MODU
# =========================

# True = sadece Telegram sinyali
# False = otomatik alım aktif

SIGNAL_ONLY = True
