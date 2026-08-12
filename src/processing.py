from typing import List, Dict, Any

def filter_by_state(list_dicts: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по значению ключа "state".
    :param list_dicts: список словарей, каждый из которых содержит ключ "state"
    :param state: значение для фильтрации (по умолчанию "EXECUTED")
    :return: новый список словарей с указанным состоянием
    """
    return [item for item in list_dicts if item.get("state") == state]
# test comment
