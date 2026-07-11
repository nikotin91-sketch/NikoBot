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

    print(
        "🚀 BTCTurk AI Scanner V3 Başladı"
    )


    create_tables()


    while True:

        try:

            print(
                "Piyasa taranıyor..."
            )


            signals = scan_market()


            if signals:

                for signal in signals:

                    save_signal(
                        signal
                    )


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
                "Ana sistem hatası:",
                e
            )


        time.sleep(
            SCAN_INTERVAL
        )




if __name__ == "__main__":


    thread = threading.Thread(
        target=bot_loop
    )

    thread.start()


    app.run(
        host="0.0.0.0",
        port=10000
    )
