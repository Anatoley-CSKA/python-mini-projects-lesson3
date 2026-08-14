from typing import List, Dict, Any


def filter_by_state(
    list_dicts: List[Dict[str, Any]], state: str = "EXECUTED"
) -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по значению ключа "state".
    :param list_dicts: список словарей с ключом "state"
    :param state: значение для фильтрации (по умолчанию "EXECUTED")
    :return: отфильтрованный список словарей
    """
    return [item for item in list_dicts if item.get("state") == state]


def sort_by_date(
    list_dicts: List[Dict[str, Any]], descending: bool = True
) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по ключу "date".
    :param list_dicts: список словарей с ключом "date"
    :param descending: True — по убыванию (новые сверху)
    :return: отсортированный список словарей
    """
    return sorted(
        list_dicts, key=lambda x: x.get("date", ""), reverse=descending
    )
