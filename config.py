import os


# Telegram ayarları

TELEGRAM_TOKEN = os.getenv(
    "TELEGRAM_TOKEN",
    ""
)

TELEGRAM_CHAT_ID = os.getenv(
    "TELEGRAM_CHAT_ID",
    ""
)



# BtcTurk API

BTCTURK_API_KEY = os.getenv(
    "BTCTURK_API_KEY",
    ""
)

BTCTURK_SECRET = os.getenv(
    "BTCTURK_SECRET",
    ""
)



# Bot çalışma modu

TRADING_MODE = os.getenv(
    "TRADING_MODE",
    "signal"
)



# AI puan ayarları

BUY_SCORE = 85

WATCH_SCORE = 70



# Risk ayarı

MAX_POSITION_PERCENT = 10



# Tarama süresi

SCAN_INTERVAL = 900
