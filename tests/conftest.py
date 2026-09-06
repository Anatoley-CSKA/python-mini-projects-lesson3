import pytest

# ===== Фикстуры для masks =====

@pytest.fixture
def valid_card_number():
    """Фикстура: корректный номер карты."""
    return "7000792289606361"


@pytest.fixture
def valid_account_number():
    """Фикстура: корректный номер счета."""
    return "73654108430135874305"


@pytest.fixture
def card_number_with_spaces():
    """Фикстура: номер карты с пробелами."""
    return "7000 7922 8960 6361"


@pytest.fixture
def account_number_with_spaces():
    """Фикстура: номер счета с пробелами."""
    return "7365 4108 4301 3587 4305"


@pytest.fixture
def invalid_card_number():
    """Фикстура: некорректный номер карты (короткий)."""
    return "1234567890"


@pytest.fixture
def invalid_account_number():
    """Фикстура: некорректный номер счета (короткий)."""
    return "123"


# ===== Фикстуры для widget =====

@pytest.fixture
def visa_platinum():
    """Фикстура: данные карты Visa Platinum."""
    return ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361")


@pytest.fixture
def maestro():
    """Фикстура: данные карты Maestro."""
    return ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199")


@pytest.fixture
def mastercard():
    """Фикстура: данные карты MasterCard."""
    return ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758")


@pytest.fixture
def account():
    """Фикстура: данные счета."""
    return ("Счет 73654108430135874305", "Счет **4305")


@pytest.fixture
def invalid_widget_data():
    """Фикстура: некорректные данные для widget."""
    return "InvalidInputWithoutSpace"


# ===== Фикстуры для processing =====

@pytest.fixture
def sample_data_mixed_states():
    """Фикстура: список словарей с разными статусами."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2021-01-01"},
        {"id": 2, "state": "CANCELED", "date": "2020-12-31"},
        {"id": 3, "state": "EXECUTED", "date": "2021-01-02"},
        {"id": 4, "state": "PENDING", "date": "2021-01-03"},
        {"id": 5, "state": "EXECUTED", "date": "2020-12-30"},
    ]


@pytest.fixture
def sample_data_executed_only():
    """Фикстура: список словарей только со статусом EXECUTED."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2021-01-01"},
        {"id": 2, "state": "EXECUTED", "date": "2020-12-31"},
        {"id": 3, "state": "EXECUTED", "date": "2021-01-02"},
    ]


@pytest.fixture
def sample_data_no_executed():
    """Фикстура: список словарей без статуса EXECUTED."""
    return [
        {"id": 1, "state": "CANCELED", "date": "2021-01-01"},
        {"id": 2, "state": "PENDING", "date": "2020-12-31"},
        {"id": 3, "state": "CANCELED", "date": "2021-01-02"},
    ]


@pytest.fixture
def sample_data_missing_key():
    """Фикстура: список словарей, где в некоторых отсутствует ключ state."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2021-01-01"},
        {"id": 2, "date": "2020-12-31"},
        {"id": 3, "state": "EXECUTED", "date": "2021-01-02"},
        {"id": 4, "date": "2021-01-03"},
    ]


@pytest.fixture
def sample_data_mixed_dates():
    """Фикстура: список словарей с разными датами."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2021-01-01"},
        {"id": 2, "state": "CANCELED", "date": "2020-12-31"},
        {"id": 3, "state": "EXECUTED", "date": "2021-01-02"},
        {"id": 4, "state": "PENDING", "date": "2021-01-03"},
    ]


@pytest.fixture
def sample_data_same_dates():
    """Фикстура: список словарей с одинаковыми датами."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2021-01-01"},
        {"id": 2, "state": "CANCELED", "date": "2021-01-01"},
        {"id": 3, "state": "PENDING", "date": "2020-12-31"},
    ]


@pytest.fixture
def sample_data_empty():
    """Фикстура: пустой список."""
    return []


@pytest.fixture
def sample_data_invalid_dates():
    """Фикстура: список словарей с некорректными форматами дат."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2021-01-01"},
        {"id": 2, "state": "CANCELED", "date": "invalid-date"},
        {"id": 3, "state": "EXECUTED", "date": "2020-12-31"},
        {"id": 4, "state": "PENDING", "date": "2021/01/03"},
    ]


@pytest.fixture
def sample_data_mixed_types():
    """Фикстура: список словарей со смешанными типами данных в ключе date."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2021-01-01"},
        {"id": 2, "state": "CANCELED", "date": 123},
        {"id": 3, "state": "EXECUTED", "date": "2020-12-31"},
    ]
