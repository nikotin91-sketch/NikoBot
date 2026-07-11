import time
import threading

from flask import Flask

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

    return "BTCTurk AI Scanner V3 aktif"



def bot_loop():

    print("🚀 BTCTurk AI Scanner V3 Başladı")

    print("1 - BOT DÖNGÜSÜ BAŞLADI")


    try:

        print("2 - DATABASE OLUŞTURULUYOR")

        create_tables()

        print("3 - DATABASE HAZIR")


    except Exception as e:

        print(
            "DATABASE HATASI:",
            e
        )

        return



    while True:

        try:

            print("4 - PİYASA TARAMA BAŞLIYOR")


            signals = scan_market()


            print(
                "5 - TARAMA BİTTİ. SİNYAL:",
                len(signals)
            )


            if signals:

                for signal in signals:

                    print(
                        "SİNYAL:",
                        signal
                    )


                    save_signal(signal)


                    message = format_signal(
                        signal
                    )


                    send_message(
                        message
                    )


            else:

                print(
                    "Güçlü sinyal yok"
                )


        except Exception as e:

            print(
                "ANA SİSTEM HATASI:",
                e
            )


        print(
            "Bekleme:",
            SCAN_INTERVAL
        )


        time.sleep(
            SCAN_INTERVAL
        )



if __name__ == "__main__":


    thread = threading.Thread(
        target=bot_loop,
        daemon=True
    )


    thread.start()


    app.run(
        host="0.0.0.0",
        port=10000
    )
