import pytest
from src.widget import mask_account_card, get_date

# Параметризованные тесты для mask_account_card
@pytest.mark.parametrize("input_data, expected_output", [
    # Стандартные карты
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    # Счета
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("Счет 35383033474447895560", "Счет **5560"),
])
def test_mask_account_card_parametrized(input_data, expected_output):
    """Параметризованный тест для проверки маскировки карт и счетов."""
    assert mask_account_card(input_data) == expected_output

def test_mask_account_card_card_only():
    """Тестирование маскировки карты."""
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"

def test_mask_account_card_account_only():
    """Тестирование маскировки счета."""
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"
    assert mask_account_card("Счет 64686473678894779589") == "Счет **9589"

def test_mask_account_card_invalid_format():
    """Обработка некорректного формата входных данных."""
    with pytest.raises(ValueError, match="Неверный формат строки: должно быть 'тип номер'"):
        mask_account_card("InvalidInputWithoutSpace")

def test_mask_account_card_invalid_type():
    """Обработка некорректного типа (не карта и не счёт)."""
    with pytest.raises(ValueError, match="Номер должен содержать только цифры"):
        mask_account_card("UnknownType 12345abcde67890")

def test_mask_account_card_short_number():
    """Обработка слишком короткого номера."""
    with pytest.raises(ValueError, match="Номер слишком короткий"):
        mask_account_card("Visa 123")

def test_mask_account_card_empty():
    """Обработка пустой строки."""
    with pytest.raises(ValueError, match="Неверный формат строки: должно быть 'тип номер'"):
        mask_account_card("")

def test_mask_account_card_with_spaces():
    """Обработка номера с пробелами."""
    # Если функция оставляет пробелы, ожидаем маску с пробелами
    assert mask_account_card("Visa Platinum 7000 7922 8960 6361") == "Visa Platinum 7000 79** **** 6361"
