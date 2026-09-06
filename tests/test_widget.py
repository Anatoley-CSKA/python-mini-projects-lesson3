import pytest
from src.widget import mask_account_card, get_date

# ===== Параметризованные тесты для mask_account_card =====

@pytest.mark.parametrize("input_data, expected_output", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("Счет 35383033474447895560", "Счет **5560"),
])
def test_mask_account_card_parametrized(input_data, expected_output):
    """Параметризованный тест для mask_account_card."""
    assert mask_account_card(input_data) == expected_output


# ===== Тесты на ошибки =====

@pytest.mark.parametrize("invalid_input, expected_error", [
    ("InvalidInputWithoutSpace", "Неверный формат строки: должно быть 'тип номер'"),
    ("", "Неверный формат строки: должно быть 'тип номер'"),
])
def test_mask_account_card_invalid_format(invalid_input, expected_error):
    with pytest.raises(ValueError, match=expected_error):
        mask_account_card(invalid_input)


@pytest.mark.parametrize("invalid_input, expected_error", [
    ("Visa 123", "Номер слишком короткий"),
    ("UnknownType 12345abcde67890", "Номер должен содержать только цифры"),
])
def test_mask_account_card_invalid_data(invalid_input, expected_error):
    with pytest.raises(ValueError, match=expected_error):
        mask_account_card(invalid_input)


@pytest.mark.parametrize("card_number, expected_output", [
    ("7000 7922 8960 6361", "Visa Platinum 7000 7922 8960 **6361"),
    ("7000792289606361", "Visa Platinum 7000 79** **** 6361"),
])
def test_mask_account_card_with_spaces(card_number, expected_output):
    assert mask_account_card(f"Visa Platinum {card_number}") == expected_output


# ===== Параметризованные тесты для get_date =====

@pytest.mark.parametrize("input_date, expected_output", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2023-12-25T10:30:00.000000", "25.12.2023"),
    ("2022-01-01T00:00:00.000000", "01.01.2022"),
    ("2024-03-11", "11.03.2024"),
    ("2024-03-11T02:26:18+03:00", "11.03.2024"),
    ("2024-03-11T02:26:18.123456", "11.03.2024"),
])
def test_get_date_valid(input_date, expected_output):
    assert get_date(input_date) == expected_output


@pytest.mark.parametrize("invalid_date", [
    "2024/03/11",
    "not a date",
    "",
])
def test_get_date_invalid(invalid_date):
    with pytest.raises(ValueError):
        get_date(invalid_date)
