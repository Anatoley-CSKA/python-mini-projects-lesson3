from src.processing import filter_by_state, sort_by_date


def test_filter_by_state():
    data = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "EXECUTED"},
    ]
    result = filter_by_state(data)
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)


def test_filter_by_state_custom():
    data = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
    ]
    result = filter_by_state(data, "CANCELED")
    assert len(result) == 1
    assert result[0]["state"] == "CANCELED"


def test_sort_by_date_descending():
    data = [
        {"date": "2021-01-01"},
        {"date": "2020-12-31"},
        {"date": "2021-01-02"},
    ]
    result = sort_by_date(data)
    assert result[0]["date"] == "2021-01-02"
    assert result[1]["date"] == "2021-01-01"
    assert result[2]["date"] == "2020-12-31"


def test_sort_by_date_ascending():
    data = [
        {"date": "2021-01-01"},
        {"date": "2020-12-31"},
        {"date": "2021-01-02"},
    ]
    result = sort_by_date(data, descending=False)
    assert result[0]["date"] == "2020-12-31"
    assert result[1]["date"] == "2021-01-01"
    assert result[2]["date"] == "2021-01-02"


def test_sort_by_date_missing_key():
    data = [
        {"id": 1},
        {"date": "2021-01-01"},
    ]
    result = sort_by_date(data)
    assert result[0]["date"] == "2021-01-01"
    assert "date" not in result[1]
