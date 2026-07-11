import os


# ======================
# API AYARLARI
# ======================

BTCTURK_API_KEY = os.getenv(
    "BTCTURK_API_KEY",
    ""
)

BTCTURK_SECRET = os.getenv(
    "BTCTURK_SECRET",
    ""
)



# ======================
# TELEGRAM
# ======================

TELEGRAM_TOKEN = os.getenv(
    "TELEGRAM_TOKEN",
    ""
)

TELEGRAM_CHAT_ID = os.getenv(
    "TELEGRAM_CHAT_ID",
    ""
)



# ======================
# ÇALIŞMA MODU
# ======================

# signal = sadece alarm
# paper = sanal işlem
# live = gerçek işlem

TRADING_MODE = os.getenv(
    "TRADING_MODE",
    "signal"
)



# ======================
# AI AYARLARI
# ======================

BUY_SCORE = 85

WATCH_SCORE = 70



# ======================
# RİSK AYARLARI
# ======================

MAX_POSITION_PERCENT = 10



# ======================
# TARAMA
# ======================

SCAN_INTERVAL = 60
