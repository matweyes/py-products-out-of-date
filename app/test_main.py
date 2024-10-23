import pytest
import datetime
from unittest.mock import patch
from app.main import outdated_products


@pytest.fixture()
def products() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]


@patch("app.main.datetime.date")
@pytest.mark.parametrize(
    "test_date, expected",
    [
        (datetime.date(2022, 2, 5), ["duck"]),
        (datetime.date(2022, 2, 10), ["chicken", "duck"]),
        (datetime.date(2022, 2, 11), ["salmon", "chicken", "duck"]),
        (datetime.date(2022, 2, 1), []),
    ]
)
def test_outdated_products(
        mocked_date: patch,
        test_date: datetime.date,
        expected: list,
        products: list
) -> None:
    mocked_date.today.return_value = test_date
    result = outdated_products(products)
    assert result == expected, f"Expected {expected}, got {result}"
