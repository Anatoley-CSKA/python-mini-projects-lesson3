import pytest
from src.processing import filter_by_state, sort_by_date

# ===== Тесты для filter_by_state =====

@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 2),
    ("CANCELED", 1),
    ("PENDING", 1),
])
def test_filter_by_state_parametrized(state, expected_count):
    """Параметризованный тест для filter_by_state."""
    data = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "EXECUTED"},
        {"id": 4, "state": "PENDING"},
    ]
    result = filter_by_state(data, state)
    assert len(result) == expected_count
    assert all(item["state"] == state for item in result)


def test_filter_by_state_default():
    """Тестирование filter_by_state с параметром по умолчанию (EXECUTED)."""
    data = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "EXECUTED"},
    ]
    result = filter_by_state(data)
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)


def test_filter_by_state_no_matches():
    """Тестирование filter_by_state при отсутствии словарей с указанным статусом."""
    data = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
    ]
    result = filter_by_state(data, "PENDING")
    assert result == []


def test_filter_by_state_missing_key():
    """Тестирование filter_by_state, когда в некоторых словарях отсутствует ключ state."""
    data = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3},  # без ключа state
    ]
    result = filter_by_state(data)
    assert len(result) == 1
    assert result[0]["id"] == 1
    assert result[0]["state"] == "EXECUTED"


def test_filter_by_state_empty_list():
    """Тестирование filter_by_state на пустом списке."""
    result = filter_by_state([])
    assert result == []


def test_filter_by_state_case_sensitive():
    """Тестирование filter_by_state на регистрозависимость."""
    data = [
        {"id": 1, "state": "executed"},  # маленькие буквы
        {"id": 2, "state": "EXECUTED"},  # большие буквы
    ]
    result = filter_by_state(data)
    # Должен найти только точное совпадение
    assert len(result) == 1
    assert result[0]["id"] == 2
