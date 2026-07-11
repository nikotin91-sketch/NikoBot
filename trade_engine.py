from config import TRADING_MODE

from database import save_trade

from btcturk_trade import place_order



def execute_buy(
    symbol,
    price,
    amount
):

    if TRADING_MODE == "signal":

        print(
            "Sinyal modu:",
            symbol
        )

        return {
            "status": "signal_only"
        }



    if TRADING_MODE == "paper":

        save_trade(
            symbol,
            "BUY",
            price,
            amount,
            "PAPER_OPEN"
        )

        return {
            "status": "paper_buy",
            "symbol": symbol
        }




    if TRADING_MODE == "live":

        result = place_order(
            symbol,
            "BUY",
            amount,
            price
        )

        return result




def execute_sell(
    symbol,
    price,
    amount
):


    if TRADING_MODE == "signal":

        return {
            "status": "signal_only"
        }



    if TRADING_MODE == "paper":

        save_trade(
            symbol,
            "SELL",
            price,
            amount,
            "PAPER_CLOSE"
        )

        return {
            "status": "paper_sell"
        }




    if TRADING_MODE == "live":

        result = place_order(
            symbol,
            "SELL",
            amount,
            price
        )

        return result
