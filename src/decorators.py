"""Модуль с декораторами для логирования вызовов функций."""
import functools
from typing import Any, Callable


def log(filename: str = "") -> Callable:
    """Декоратор для логирования вызовов функций.

    Записывает имя функции, аргументы и результат или ошибку
    в файл (если указан filename) или выводит в консоль.

    :param filename: путь к файлу для логов (если пусто — вывод в консоль)
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            args_str = ", ".join(repr(a) for a in args)
            kwargs_str = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
            params = ", ".join(filter(None, [args_str, kwargs_str]))

            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__}({params}) -> {result!r}\n"
            except Exception as e:
                message = (
                    f"{func.__name__}({params}) -> ERROR: "
                    f"{type(e).__name__}: {e}\n"
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
