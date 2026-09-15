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


def card_number_generator(start: int, end: int):
    """Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX.

    :param start: начальное значение диапазона (включительно)
    :param end: конечное значение диапазона (включительно)
    :yield: строка с номером карты
    """
    for number in range(start, end + 1):
        card_str = f"{number:016d}"
        formatted = " ".join(
            card_str[i:i + 4] for i in range(0, 16, 4)
        )
        yield formatted
