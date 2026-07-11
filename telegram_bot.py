import requests

from config import (
    TELEGRAM_TOKEN,
    TELEGRAM_CHAT_ID
)



def send_message(message):

    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print(
            "Telegram ayarları eksik"
        )
        return False


    url = (
        f"https://api.telegram.org/"
        f"bot{TELEGRAM_TOKEN}/sendMessage"
    )


    payload = {

        "chat_id": TELEGRAM_CHAT_ID,

        "text": message,

        "parse_mode": "HTML"

    }


    try:

        response = requests.post(
            url,
            json=payload,
            timeout=10
        )


        return response.status_code == 200


    except Exception as e:

        print(
            "Telegram hata:",
            e
        )

        return False




def format_signal(data):

    reasons = "\n".join(
        [
            "✅ " + x
            for x in data["reasons"]
        ]
    )


    text = f"""

🚀 <b>AI BUY SİNYALİ</b>


Coin:
<b>{data['symbol']}</b>


Skor:
<b>{data['score']}/100</b>


Fiyat:
<b>{data['price']}</b>


Neden:

{reasons}


🛑 Stop:
{data['stop']}


🎯 Hedef 1:
{data['target1']}


🎯 Hedef 2:
{data['target2']}


Risk/Ödül:
{data['risk_reward']}

"""


    return text
