from typing import List, Dict, Any

def filter_by_state(list_dicts: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по значению ключа "state".
    """
    return [item for item in list_dicts if item.get("state") == state]


def sort_by_date(list_dicts: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по ключу "date".
    :param list_dicts: список словарей, каждый из которых содержит ключ "date"
    :param descending: True — по убыванию (новые сверху), False — по возрастанию
    :return: новый отсортированный список
    """
    return sorted(list_dicts, key=lambda x: x.get("date", ""), reverse=descending)