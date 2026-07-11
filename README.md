# BTCTurk AI Scanner V3

BtcTurk TRY marketleri için yapay zeka destekli kripto tarama botu.

## Özellikler

- Tüm TRY coin çiftlerini tarama
- RSI analizi
- EMA trend analizi
- MACD analizi
- ATR risk hesabı
- Hacim patlaması algılama
- AI skor sistemi
- Telegram bildirimleri
- Paper trading altyapısı
- Al-sat altyapısı


## Çalışma Modları

### Signal Mode

Sadece sinyal üretir, işlem açmaz.

TRADING_MODE=signal


### Paper Mode

Sanal işlem yapar.

TRADING_MODE=paper


### Live Mode

Gerçek işlem altyapısı.

TRADING_MODE=live


## Kurulum

Gerekli kütüphaneleri yükle:

pip install -r requirements.txt


Botu çalıştır:

python app.py


## Ayarlar

Gerekli bilgiler:

BTCTURK_API_KEY=

BTCTURK_SECRET=

TELEGRAM_TOKEN=

TELEGRAM_CHAT_ID=

TRADING_MODE=signal


## Sistem Akışı

BtcTurk API

↓

Scanner

↓

Indicators

↓

AI Engine

↓

Risk Manager

↓

Telegram / Trade Engine


## Proje Durumu

V3 geliştirme aşamasındadır.

Amaç:
BtcTurk TRY piyasalarında güçlü fırsatları analiz edip kullanıcıya bildiren AI destekli tarama sistemi oluşturmaktır.
