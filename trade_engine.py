from config import TRADING_MODE

from database import (
    connect
)


def open_trade(
    symbol,
    price,
    amount
):

    if TRADING_MODE == "signal":

        print(
            "SIGNAL MODE:",
            symbol,
            price
        )

        return {
            "status": "signal",
            "symbol": symbol,
            "price": price
        }



    if TRADING_MODE == "paper":

        save_trade(
            symbol,
            "BUY",
            price,
            amount,
            "OPEN"
        )

        return {
            "status": "paper_open",
            "symbol": symbol,
            "price": price
        }



    if TRADING_MODE == "live":

        # Gerçek emir bağlantısı
        # BtcTurk private API buraya eklenecek

        return {
            "status": "live_not_ready"
        }





def close_trade(
    symbol,
    price
):

    save_trade(
        symbol,
        "SELL",
        price,
        0,
        "CLOSED"
    )


    return {
        "status": "closed",
        "symbol": symbol,
        "price": price
    }





def save_trade(
    symbol,
    side,
    price,
    amount,
    status
):

    conn = connect()

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO trades
        (
        symbol,
        side,
        price,
        amount,
        status,
        time
        )
        VALUES (?,?,?,?,?,datetime('now'))
        """,

        (
        symbol,
        side,
        price,
        amount,
        status
        )

    )


    conn.commit()

    conn.close()
