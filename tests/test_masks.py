import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number_standard(valid_card_number):
    """Тестирование правильности маскирования номера карты."""
    assert get_mask_card_number(valid_card_number) == "7000 79** **** 6361"


def test_get_mask_card_number_with_spaces(card_number_with_spaces):
    """Проверка обработки номера с пробелами."""
    assert get_mask_card_number(card_number_with_spaces) == "7000 79** **** 6361"


def test_get_mask_card_number_invalid(invalid_card_number):
    """Тестирование обработки некорректного номера."""
    with pytest.raises(ValueError, match="Card number must contain 16 digits"):
        get_mask_card_number(invalid_card_number)


def test_get_mask_account_standard(valid_account_number):
    """Тестирование правильности маскирования номера счета."""
    assert get_mask_account(valid_account_number) == "**4305"


def test_get_mask_account_with_spaces(account_number_with_spaces):
    """Проверка обработки номера счета с пробелами."""
    assert get_mask_account(account_number_with_spaces) == "**4305"


def test_get_mask_account_invalid(invalid_account_number):
    """Тестирование обработки некорректного номера счета."""
    with pytest.raises(ValueError, match="Account number must contain at least 4 digits"):
        get_mask_account(invalid_account_number)
