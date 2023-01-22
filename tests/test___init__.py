from datetime import datetime

from custom_components.som_energia.price import price, compensation


def test_price_on_monday():
    monday = datetime(2022, 1, 24, 0, 0, 0)
    assert price(monday) == 0.234

    monday = datetime(2022, 1, 24, 8, 0, 0)
    assert price(monday) == 0.281

    monday = datetime(2022, 1, 24, 10, 0, 0)
    assert price(monday) == 0.343


def test_price_on_sunday():
    sunday = datetime(2022, 1, 23, 16, 57, 0)
    assert price(sunday) == 0.234

def test_compesation():
    assert compensation() == 0.176


def test_price_on_holiday():
    holiday = datetime(2023, 1, 6, 16, 57, 0)
    assert price(holiday) == 0.284556
