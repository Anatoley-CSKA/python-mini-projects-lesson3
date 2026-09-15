from typing import Any, Dict, Iterator, List


def filter_by_currency(
    transactions: List[Dict[str, Any]],
    currency: str,
) -> Iterator[Dict[str, Any]]:
    """Фильтрует транзакции по коду валюты.

    :param transactions: список словарей с транзакциями
    :param currency: код валюты (например, "USD")
    :return: итератор с транзакциями, у которых валюта совпадает
    """
    for transaction in transactions:
        code = (
            transaction.get("operationAmount", {})
            .get("currency", {})
            .get("code")
        )
        if code == currency:
            yield transaction


def transaction_descriptions(transactions):
    """Возвращает описания транзакций по очереди.

    :param transactions: список словарей с транзакциями
    :return: итератор с описаниями транзакций
    """
    for transaction in transactions:
        yield transaction.get("description", "")
