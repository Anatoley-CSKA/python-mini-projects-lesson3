import pytest

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
        {"id": 2, "date": "2020-12-31"},  # нет state
        {"id": 3, "state": "EXECUTED", "date": "2021-01-02"},
        {"id": 4, "date": "2021-01-03"},  # нет state
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
        {"id": 4, "state": "PENDING", "date": "2021/01/03"},  # нестандартный формат
    ]


@pytest.fixture
def sample_data_mixed_types():
    """Фикстура: список словарей со смешанными типами данных в ключе date."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2021-01-01"},
        {"id": 2, "state": "CANCELED", "date": 123},  # число вместо строки
        {"id": 3, "state": "EXECUTED", "date": "2020-12-31"},
    ]
