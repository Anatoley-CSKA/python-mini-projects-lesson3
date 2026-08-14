# Python Mini Projects — Lesson 3

## Описание проекта
Проект содержит функцию filter_by_state для фильтрации списка словарей.

## Установка и запуск
1. Клонируйте репозиторий
2. Установите зависимости: poetry install
3. Запустите тесты: poetry run pytest

## Пример использования
from src.processing import filter_by_state
data = [{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "CANCELED"}]
print(filter_by_state(data))  # [{"id": 1, "state": "EXECUTED"}]
