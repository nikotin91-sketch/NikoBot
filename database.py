import sqlite3
from datetime import datetime


DB_NAME = "scanner.db"



def connect():

    return sqlite3.connect(
        DB_NAME
    )



def create_tables():

    conn = connect()

    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS signals (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        symbol TEXT,

        signal TEXT,

        score INTEGER,

        price REAL,

        time TEXT

    )
    """)



    cursor.execute("""
    CREATE TABLE IF NOT EXISTS trades (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        symbol TEXT,

        side TEXT,

        price REAL,

        amount REAL,

        status TEXT,

        time TEXT

    )
    """)



    conn.commit()

    conn.close()




def save_signal(data):

    conn = connect()

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO signals
        (
        symbol,
        signal,
        score,
        price,
        time
        )
        VALUES (?,?,?,?,?)
        """,

        (
            data["symbol"],
            data["signal"],
            data["score"],
            data["price"],
            datetime.now().isoformat()
        )
    )


    conn.commit()

    conn.close()




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
        VALUES (?,?,?,?,?,?)
        """,

        (
            symbol,
            side,
            price,
            amount,
            status,
            datetime.now().isoformat()
        )
    )


    conn.commit()

    conn.close()




def recent_signal(symbol):

    conn = connect()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT *
        FROM signals
        WHERE symbol=?
        ORDER BY id DESC
        LIMIT 1
        """,

        (symbol,)
    )


    result = cursor.fetchone()


    conn.close()


    return result




def can_send_signal(symbol, signal, cooldown=300):

    conn = connect()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT time
        FROM signals
        WHERE symbol=?
        AND signal=?
        ORDER BY id DESC
        LIMIT 1
        """,

        (
            symbol,
            signal
        )
    )


    result = cursor.fetchone()


    conn.close()



    if not result:

        return True



    last_time = datetime.fromisoformat(
        result[0]
    )



    now = datetime.now()



    diff = (
        now - last_time
    ).total_seconds()



    if diff >= cooldown:

        return True



    return False




def get_trades():

    conn = connect()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT *
        FROM trades
        ORDER BY id DESC
        """
    )


    result = cursor.fetchall()


    conn.close()


    return result
