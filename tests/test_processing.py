import pytest
from src.processing import filter_by_state, sort_by_date

# ===== Тесты для filter_by_state =====

@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 3),
    ("CANCELED", 1),
    ("PENDING", 1),
])
def test_filter_by_state_parametrized(sample_data_mixed_states, state, expected_count):
    """Параметризованный тест для filter_by_state."""
    result = filter_by_state(sample_data_mixed_states, state)
    assert len(result) == expected_count
    assert all(item["state"] == state for item in result)


def test_filter_by_state_default(sample_data_mixed_states):
    """Тестирование filter_by_state с параметром по умолчанию (EXECUTED)."""
    result = filter_by_state(sample_data_mixed_states)
    assert len(result) == 3
    assert all(item["state"] == "EXECUTED" for item in result)


def test_filter_by_state_no_matches(sample_data_no_executed):
    """Тестирование filter_by_state при отсутствии словарей с указанным статусом."""
    result = filter_by_state(sample_data_no_executed, "EXECUTED")
    assert result == []


def test_filter_by_state_missing_key(sample_data_missing_key):
    """Тестирование filter_by_state, когда в некоторых словарях отсутствует ключ state."""
    result = filter_by_state(sample_data_missing_key)
    # Должен найти только словари с ключом state == "EXECUTED"
    assert len(result) == 2
    assert all("state" in item for item in result)
    assert all(item["state"] == "EXECUTED" for item in result)


def test_filter_by_state_empty_list(sample_data_empty):
    """Тестирование filter_by_state на пустом списке."""
    result = filter_by_state(sample_data_empty)
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

def test_sort_by_date_descending(sample_data_mixed_dates):
    """Тестирование сортировки по датам в порядке убывания (по умолчанию)."""
    result = sort_by_date(sample_data_mixed_dates)
    dates = [item["date"] for item in result]
    assert dates == ["2021-01-03", "2021-01-02", "2021-01-01", "2020-12-31"]


def test_sort_by_date_ascending(sample_data_mixed_dates):
    """Тестирование сортировки по датам в порядке возрастания."""
    result = sort_by_date(sample_data_mixed_dates, descending=False)
    dates = [item["date"] for item in result]
    assert dates == ["2020-12-31", "2021-01-01", "2021-01-02", "2021-01-03"]


def test_sort_by_date_same_dates(sample_data_same_dates):
    """Тестирование сортировки при одинаковых датах (порядок должен сохраняться)."""
    result = sort_by_date(sample_data_same_dates)
    # Проверяем, что даты отсортированы правильно
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


def test_sort_by_date_invalid_format(sample_data_invalid_dates):
    """Тестирование сортировки с некорректным форматом даты."""
    result = sort_by_date(sample_data_invalid_dates)
    # Проверяем, что функция не падает и возвращает список
    assert len(result) == 4
    # Проверяем, что все элементы сохранены
    assert all(isinstance(item, dict) for item in result)


def test_sort_by_date_empty_list(sample_data_empty):
    """Тестирование сортировки пустого списка."""
    result = sort_by_date(sample_data_empty)
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


def test_sort_by_date_mixed_types(sample_data_mixed_types):
    """Тестирование сортировки при смешанных типах данных в ключе date."""
    # Функция должна выбросить TypeError или обработать смешанные типы
    with pytest.raises(TypeError):
        sort_by_date(sample_data_mixed_types)
