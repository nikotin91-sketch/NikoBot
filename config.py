# BTCTurk AI Scanner V3
# Configuration

import os


# Çalışma modu
# signal  -> sadece sinyal
# paper   -> sanal işlem
# live    -> gerçek işlem
TRADING_MODE = os.getenv("TRADING_MODE", "signal")


# BtcTurk API
BTCTURK_API_KEY = os.getenv("BTCTURK_API_KEY", "")
BTCTURK_SECRET = os.getenv("BTCTURK_SECRET", "")


# Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")


# Tarama ayarları

# Tüm TRY marketleri taranacak
QUOTE_CURRENCY = "TRY"

# Kaç saniyede bir tarama
SCAN_INTERVAL = 60


# AI skor ayarları

BUY_SCORE = 85
WATCH_SCORE = 70


# Risk yönetimi

# Tek işlemde kullanılacak maksimum oran
MAX_POSITION_PERCENT = 10

# Stop seviyesi
STOP_LOSS_PERCENT = 2.5

# Hedef
TAKE_PROFIT_PERCENT = 5


# Teknik ayarlar

RSI_PERIOD = 14

EMA_FAST = 9
EMA_MID = 21
EMA_SLOW = 50

MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9


# Mod

AGGRESSIVE_MODE = True


print("BTCTurk AI Scanner V3 Config Loaded")
print("Mode:", TRADING_MODE)
