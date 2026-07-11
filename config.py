import os


# Tarama aralığı (saniye)
SCAN_INTERVAL = int(
    os.getenv(
        "SCAN_INTERVAL",
        60
    )
)


# Aynı coin aynı sinyal tekrar süresi
# 300 saniye = 5 dakika
SIGNAL_COOLDOWN = int(
    os.getenv(
        "SIGNAL_COOLDOWN",
        300
    )
)



# Telegram ayarları

TELEGRAM_TOKEN = os.getenv(
    "TELEGRAM_TOKEN"
)


TELEGRAM_CHAT_ID = os.getenv(
    "TELEGRAM_CHAT_ID"
)



# BtcTurk API

BTCTURK_API_KEY = os.getenv(
    "BTCTURK_API_KEY"
)


BTCTURK_SECRET = os.getenv(
    "BTCTURK_SECRET"
)
