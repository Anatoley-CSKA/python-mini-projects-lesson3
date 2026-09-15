import pytest
from src.generators import filter_by_currency


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 939719570,
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Transfer to organization",
        },
        {
            "id": 142264268,
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Transfer from account to account",
        },
        {
            "id": 873106923,
            "operationAmount": {
                "amount": "100.00",
                "currency": {"name": "RUB", "code": "RUB"},
            },
            "description": "Transfer to organization",
        },
    ]


def test_filter_by_currency_usd(sample_transactions):
    result = list(filter_by_currency(sample_transactions, "USD"))
    assert len(result) == 2
    assert all(
        t["operationAmount"]["currency"]["code"] == "USD" for t in result
    )


def test_filter_by_currency_rub(sample_transactions):
    result = list(filter_by_currency(sample_transactions, "RUB"))
    assert len(result) == 1


def test_filter_by_currency_empty(sample_transactions):
    result = list(filter_by_currency(sample_transactions, "EUR"))
    assert result == []


def test_filter_by_currency_empty_list():
    result = list(filter_by_currency([], "USD"))
    assert result == []
