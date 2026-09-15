from typing import Any, Dict, Iterator, List


def filter_by_currency(
    transactions: List[Dict[str, Any]],
    currency: str,
) -> Iterator[Dict[str, Any]]:
    """Фильтрует транзакции по коду валюты."""
    for transaction in transactions:
        code = (
            transaction.get("operationAmount", {})
            .get("currency", {})
            .get("code")
        )
        if code == currency:
            yield transaction


def transaction_descriptions(
    transactions: List[Dict[str, Any]],
) -> Iterator[str]:
    """Возвращает описания транзакций по очереди."""
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, end + 1):
        card_str = f"{number:016d}"
        formatted = " ".join(card_str[i : i + 4] for i in range(0, 16, 4))
        yield formatted
