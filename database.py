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
