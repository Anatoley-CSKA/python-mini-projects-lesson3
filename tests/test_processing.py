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

# ===== Тесты для sort_by_date =====

def test_sort_by_date_descending():
    """Тестирование сортировки по датам в порядке убывания (по умолчанию)."""
    data = [
        {"id": 1, "date": "2021-01-01"},
        {"id": 2, "date": "2020-12-31"},
        {"id": 3, "date": "2021-01-02"},
    ]
    result = sort_by_date(data)
    assert result[0]["date"] == "2021-01-02"
    assert result[1]["date"] == "2021-01-01"
    assert result[2]["date"] == "2020-12-31"


def test_sort_by_date_ascending():
    """Тестирование сортировки по датам в порядке возрастания."""
    data = [
        {"id": 1, "date": "2021-01-01"},
        {"id": 2, "date": "2020-12-31"},
        {"id": 3, "date": "2021-01-02"},
    ]
    result = sort_by_date(data, descending=False)
    assert result[0]["date"] == "2020-12-31"
    assert result[1]["date"] == "2021-01-01"
    assert result[2]["date"] == "2021-01-02"


def test_sort_by_date_same_dates():
    """Тестирование сортировки при одинаковых датах (порядок должен сохраняться)."""
    data = [
        {"id": 1, "date": "2021-01-01"},
        {"id": 2, "date": "2021-01-01"},
        {"id": 3, "date": "2020-12-31"},
    ]
    result = sort_by_date(data)
    # Даты одинаковые — порядок сохраняется для элементов с одинаковой датой
    assert result[0]["date"] == "2021-01-01"
    assert result[1]["date"] == "2021-01-01"
    assert result[2]["date"] == "2020-12-31"
    # Проверяем, что элементы с одинаковой датой остались в исходном порядке
    assert result[0]["id"] == 1
    assert result[1]["id"] == 2


def test_sort_by_date_missing_key():
    """Тестирование сортировки, когда в некоторых словарях отсутствует ключ date."""
    data = [
        {"id": 1, "date": "2021-01-01"},
        {"id": 2},  # без ключа date
        {"id": 3, "date": "2020-12-31"},
    ]
    result = sort_by_date(data)
    # Словари без ключа date должны оказаться в конце
    assert result[0]["date"] == "2021-01-01"
    assert result[1]["date"] == "2020-12-31"
    assert "date" not in result[2]


def test_sort_by_date_invalid_format():
    """Тестирование сортировки с некорректным форматом даты."""
    data = [
        {"id": 1, "date": "2021-01-01"},
        {"id": 2, "date": "invalid-date"},
        {"id": 3, "date": "2020-12-31"},
    ]
    result = sort_by_date(data)
    # Строки с некорректным форматом должны быть отсортированы как строки
    # (но это зависит от реализации функции)
    # В текущей реализации sort_by_date использует строки, поэтому они сортируются лексикографически
    assert result[0]["date"] == "2021-01-01"
    assert result[1]["date"] == "2020-12-31"
    assert result[2]["date"] == "invalid-date"


def test_sort_by_date_empty_list():
    """Тестирование сортировки пустого списка."""
    result = sort_by_date([])
    assert result == []


def test_sort_by_date_only_missing_key():
    """Тестирование сортировки, когда все словари без ключа date."""
    data = [
        {"id": 1},
        {"id": 2},
        {"id": 3},
    ]
    result = sort_by_date(data)
    # Все словари без ключа date — порядок сохраняется
    assert len(result) == 3
    assert result[0]["id"] == 1
    assert result[1]["id"] == 2
    assert result[2]["id"] == 3
    assert all("date" not in item for item in result)


def test_sort_by_date_mixed_types():
    """Тестирование сортировки при смешанных типах данных в ключе date."""
    data = [
        {"id": 1, "date": "2021-01-01"},
        {"id": 2, "date": 123},  # число вместо строки
        {"id": 3, "date": "2020-12-31"},
    ]
    result = sort_by_date(data)
    # Смешанные типы могут привести к ошибке, но функция должна обработать это
    # или выбросить исключение. Проверяем, что функция не падает.
    assert len(result) == 3

def test_sort_by_date_invalid_format():
    """Тестирование сортировки с некорректным форматом даты."""
    data = [
        {"id": 1, "date": "2021-01-01"},
        {"id": 2, "date": "invalid-date"},
        {"id": 3, "date": "2020-12-31"},
    ]
    result = sort_by_date(data)
    # Строки сортируются лексикографически
    assert result[0]["date"] == "invalid-date"  # 'i' < '2'
    assert result[1]["date"] == "2021-01-01"
    assert result[2]["date"] == "2020-12-31"


def test_sort_by_date_mixed_types():
    """Тестирование сортировки при смешанных типах данных в ключе date."""
    import pytest
    data = [
        {"id": 1, "date": "2021-01-01"},
        {"id": 2, "date": 123},  # число вместо строки
        {"id": 3, "date": "2020-12-31"},
    ]
    with pytest.raises(TypeError):
        sort_by_date(data)
