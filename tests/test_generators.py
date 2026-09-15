import pytest
from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
)


# ============================================================
# Тесты для filter_by_currency
# ============================================================

@pytest.fixture
def sample_transactions():
    """Фикстура: список транзакций с разными валютами."""
    return [
        {
            "id": 939719570,
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
        },
        {
            "id": 142264268,
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
        },
        {
            "id": 873106923,
            "operationAmount": {
                "amount": "100.00",
                "currency": {"name": "RUB", "code": "RUB"},
            },
            "description": "Перевод организации",
        },
    ]


def test_filter_by_currency_usd(sample_transactions):
    """Фильтрация по USD."""
    result = list(filter_by_currency(sample_transactions, "USD"))
    assert len(result) == 2
    assert all(
        t["operationAmount"]["currency"]["code"] == "USD" for t in result
    )


def test_filter_by_currency_rub(sample_transactions):
    """Фильтрация по RUB."""
    result = list(filter_by_currency(sample_transactions, "RUB"))
    assert len(result) == 1
    assert result[0]["id"] == 873106923


def test_filter_by_currency_no_match(sample_transactions):
    """Валюта отсутствует в списке."""
    result = list(filter_by_currency(sample_transactions, "EUR"))
    assert result == []


def test_filter_by_currency_empty_list():
    """Пустой список транзакций."""
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_filter_by_currency_missing_keys():
    """Транзакции без ключей operationAmount / currency."""
    transactions = [
        {"id": 1},
        {"id": 2, "operationAmount": {}},
        {"id": 3, "operationAmount": {"currency": {}}},
    ]
    result = list(filter_by_currency(transactions, "USD"))
    assert result == []


def test_filter_by_currency_returns_iterator(sample_transactions):
    """Функция возвращает итератор, а не список."""
    result = filter_by_currency(sample_transactions, "USD")
    assert not isinstance(result, list)
    assert hasattr(result, "__next__")


# ============================================================
# Тесты для transaction_descriptions
# ============================================================

@pytest.fixture
def sample_descriptions():
    """Фикстура: список транзакций с описаниями."""
    return [
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод с карты на карту"},
        {"description": "Перевод организации"},
    ]


def test_transaction_descriptions_order(sample_descriptions):
    """Проверка, что описания возвращаются по порядку."""
    descriptions = transaction_descriptions(sample_descriptions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"


def test_transaction_descriptions_all(sample_descriptions):
    """Все описания через list."""
    result = list(transaction_descriptions(sample_descriptions))
    assert len(result) == 5
    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


def test_transaction_descriptions_empty():
    """Пустой список транзакций."""
    result = list(transaction_descriptions([]))
    assert result == []


def test_transaction_descriptions_single():
    """Одна транзакция."""
    result = list(transaction_descriptions([{"description": "Один"}]))
    assert result == ["Один"]


def test_transaction_descriptions_missing_key():
    """Транзакция без ключа description."""
    transactions = [
        {"description": "Есть"},
        {},
        {"description": "Тоже есть"},
    ]
    result = list(transaction_descriptions(transactions))
    assert result == ["Есть", "", "Тоже есть"]


def test_transaction_descriptions_returns_iterator(sample_descriptions):
    """Функция возвращает итератор."""
    result = transaction_descriptions(sample_descriptions)
    assert hasattr(result, "__next__")
    assert not isinstance(result, list)


# ============================================================
# Тесты для card_number_generator
# ============================================================

def test_card_number_generator_basic():
    """Генерация с 1 по 5."""
    cards = list(card_number_generator(1, 5))
    assert cards == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]


def test_card_number_generator_single():
    """Диапазон из одного числа."""
    cards = list(card_number_generator(1, 1))
    assert cards == ["0000 0000 0000 0001"]


def test_card_number_generator_min():
    """Минимальное значение."""
    cards = list(card_number_generator(1, 1))
    assert cards[0] == "0000 0000 0000 0001"


def test_card_number_generator_max():
    """Максимальное значение."""
    cards = list(card_number_generator(9999999999999999, 9999999999999999))
    assert cards == ["9999 9999 9999 9999"]


def test_card_number_generator_empty_range():
    """Пустой диапазон (start > end)."""
    cards = list(card_number_generator(5, 4))
    assert cards == []


def test_card_number_generator_format():
    """Формат с ведущими нулями и пробелами."""
    cards = list(card_number_generator(1234567890123456, 1234567890123456))
    assert cards == ["1234 5678 9012 3456"]


def test_card_number_generator_leading_zeros():
    """Проверка ведущих нулей для маленьких чисел."""
    cards = list(card_number_generator(1, 3))
    assert cards[0] == "0000 0000 0000 0001"
    assert cards[1] == "0000 0000 0000 0002"
    assert cards[2] == "0000 0000 0000 0003"


def test_card_number_generator_grouping():
    """Проверка разбивки на группы по 4 цифры."""
    cards = list(card_number_generator(1, 1))
    parts = cards[0].split(" ")
    assert len(parts) == 4
    assert all(len(part) == 4 for part in parts)


def test_card_number_generator_10_cards():
    """Генерация 10 карт подряд."""
    cards = list(card_number_generator(1, 10))
    assert len(cards) == 10
    assert cards[0] == "0000 0000 0000 0001"
    assert cards[-1] == "0000 0000 0000 0010"


def test_card_number_generator_returns_iterator():
    """Функция возвращает итератор."""
    result = card_number_generator(1, 5)
    assert hasattr(result, "__next__")
    assert not isinstance(result, list)
