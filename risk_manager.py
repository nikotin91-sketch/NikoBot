from config import (
    MAX_POSITION_PERCENT
)


def calculate_position_size(
    balance,
    price
):
    """
    İşlem miktarını hesaplar.
    """

    if balance <= 0 or price <= 0:
        return 0


    amount = (
        balance *
        MAX_POSITION_PERCENT
        / 100
    )


    quantity = (
        amount /
        price
    )


    return round(
        quantity,
        8
    )




def calculate_stop_loss(
    entry,
    stop_percent=2.5
):

    stop = (
        entry -
        (entry * stop_percent / 100)
    )


    return round(
        stop,
        8
    )




def calculate_take_profit(
    entry,
    profit_percent=5
):

    target = (
        entry +
        (entry * profit_percent / 100)
    )


    return round(
        target,
        8
    )




def risk_check(
    balance,
    amount
):

    max_amount = (
        balance *
        MAX_POSITION_PERCENT
        / 100
    )


    if amount > max_amount:

        return False


    return True
