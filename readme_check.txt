# Python Mini Projects — Lesson 3

## 📌 Описание проекта

Проект содержит функции для работы с банковскими данными:
- Маскировка номеров карт и счетов (masks)
- Форматирование информации о картах и счетах (widget)
- Обработка данных (processing)

---

## 🧪 Тестирование

### Запуск тестов
```bash
poetry run pytest
```

### Запуск тестов с покрытием
```bash
poetry run pytest --cov=src --cov-report=term-missing
```

### Результаты тестирования

| Модуль | Количество тестов | Покрытие |
|--------|-------------------|----------|
| masks | 6 | 100% |
| widget | 24 | 100% |
| processing | 16 | 100% |
| **Итого** | **46** | **100%** |

---

## 🔄 Модуль `generators`

Модуль содержит функции-генераторы для обработки транзакций и генерации данных.

### Функция `filter_by_currency`

Фильтрует транзакции по коду валюты. Возвращает итератор, который поочерёдно выдаёт транзакции, где валюта соответствует заданной.

```python
from src.generators import filter_by_currency

transactions = [
    {
        "id": 939719570,
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
    },
    {
        "id": 873106923,
        "operationAmount": {
            "amount": "43318.34",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод со счета на счет",
    },
]

usd_transactions = filter_by_currency(transactions, "USD")
for transaction in usd_transactions:
    print(transaction)
# {'id': 939719570, 'operationAmount': {...}, 'description': 'Перевод организации'}


---

## 🔄 Модуль generators

Модуль содержит функции-генераторы для обработки транзакций.

### Функция filter_by_currency

Фильтрует транзакции по коду валюты.

Пример:
from src.generators import filter_by_currency
usd_transactions = filter_by_currency(transactions, "USD")
for transaction in usd_transactions:
    print(transaction)

### Функция transaction_descriptions

Возвращает описания транзакций по очереди.

Пример:
from src.generators import transaction_descriptions
descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

### Функция card_number_generator

Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX.

Пример:
from src.generators import card_number_generator
for card_number in card_number_generator(1, 5):
    print(card_number)
