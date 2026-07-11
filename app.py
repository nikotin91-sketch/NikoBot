from flask import Flask
import threading
import time

from database import (
    create_tables,
    save_signal
)

from scanner import (
    scan_market
)

from telegram_bot import (
    send_message,
    format_signal
)

from config import (
    SCAN_INTERVAL
)


app = Flask(__name__)


@app.route("/")
def home():
    return "BTCTurk AI Scanner V3 Sinyal Modu Aktif"


def bot_loop():

    print("🚀 SİNYAL BOTU BAŞLADI")

    try:
        create_tables()
        print("DATABASE HAZIR")

    except Exception as e:
        print("DATABASE HATASI:", e)
        return


    while True:

        try:

            print("📡 PİYASA TARAMASI BAŞLIYOR")

            signals = scan_market()

            print(
                "TARAMA BİTTİ:",
                len(signals),
                "SİNYAL"
            )


            for signal in signals:

                # Veritabanına kaydet
                save_signal(signal)


                # Telegram mesajı
                message = format_signal(signal)


                send_message(
                    message
                )


        except Exception as e:

            print(
                "BOT HATASI:",
                e
            )


        time.sleep(
            SCAN_INTERVAL
        )


if __name__ == "__main__":

    worker = threading.Thread(
        target=bot_loop
    )

    worker.daemon = True
    worker.start()


    time.sleep(2)


    app.run(
        host="0.0.0.0",
        port=10000
    )
