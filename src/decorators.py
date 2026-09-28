"""Модуль с декораторами для логирования вызовов функций."""
import functools
from typing import Any, Callable


def log(filename: str = "") -> Callable:
    """Декоратор для логирования вызовов функций.

    Логирует результат выполнения функции или ошибку. Записывает
    логи в файл, если указан filename, иначе выводит в консоль.

    :param filename: путь к файлу для логов (по умолчанию — консоль)
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok\n"
            except Exception as e:
                message = (
                    f"{func.__name__} error: {type(e).__name__}. "
                    f"Inputs: {args}, {kwargs}\n"
                )
                _write_log(filename, message)
                raise

            _write_log(filename, message)
            return result

        return wrapper

    return decorator


def _write_log(filename: str, message: str) -> None:
    """Записывает сообщение в файл или выводит в консоль."""
    if filename:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message)
    else:
        print(message, end="")
