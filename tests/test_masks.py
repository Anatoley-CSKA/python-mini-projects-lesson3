import pytest
from src.masks import get_mask_card_number

def test_get_mask_card_number_standard():
    """Тестирование правильности маскирования номера карты."""
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("1234567812345678") == "1234 56** **** 5678"

def test_get_mask_card_number_min_length():
    """Граничный случай: минимальная длина номера карты (16 цифр)."""
    assert get_mask_card_number("0000000000000000") == "0000 00** **** 0000"

def test_get_mask_card_number_max_length():
    """Граничный случай: максимальная длина (20 цифр) — должна вызывать ошибку."""
    with pytest.raises(ValueError, match="Card number must contain 16 digits"):
        get_mask_card_number("12345678901234567890")

def test_get_mask_card_number_non_standard_length():
    """Нестандартная длина номера карты (не 16 цифр)."""
    with pytest.raises(ValueError, match="Card number must contain 16 digits"):
        get_mask_card_number("1234567890")  # 10 цифр

def test_get_mask_card_number_empty():
    """Проверка обработки пустой строки."""
    with pytest.raises(ValueError, match="Card number must contain 16 digits"):
        get_mask_card_number("")

def test_get_mask_card_number_with_spaces():
    """Проверка обработки номера с пробелами."""
    # Если функция должна обрабатывать пробелы, ожидаем корректный результат
    # В противном случае выбрасываем исключение
    with pytest.raises(ValueError, match="Card number must contain 16 digits"):
        get_mask_card_number("7000 7922 8960 6361")
