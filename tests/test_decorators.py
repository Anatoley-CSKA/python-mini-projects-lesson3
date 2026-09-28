"""Тесты для декоратора log из модуля decorators."""
import os
import tempfile

import pytest

from src.decorators import log


# ============================================================
# Тесты для логирования в консоль (capsys)
# ============================================================

def test_log_success_console(capsys):
    """Успешное выполнение — вывод в консоль."""
    @log()
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)
    captured = capsys.readouterr()

    assert result == 3
    assert captured.out == "my_function ok\n"


def test_log_success_console_no_args(capsys):
    """Успешное выполнение без аргументов."""
    @log()
    def get_value():
        return 42

    result = get_value()
    captured = capsys.readouterr()

    assert result == 42
    assert captured.out == "get_value ok\n"


def test_log_error_console(capsys):
    """Ошибка — вывод в консоль."""
    @log()
    def my_function(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        my_function(1, 0)

    captured = capsys.readouterr()
    assert captured.out == (
        "my_function error: ZeroDivisionError. "
        "Inputs: (1, 0), {}\n"
    )


def test_log_error_with_kwargs(capsys):
    """Ошибка с именованными аргументами."""
    @log()
    def divide(a, b=1):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, b=0)

    captured = capsys.readouterr()
    assert captured.out == (
        "divide error: ZeroDivisionError. "
        "Inputs: (10,), {'b': 0}\n"
    )


def test_log_custom_error(capsys):
    """Пользовательская ошибка."""
    @log()
    def fail():
        raise ValueError("Что-то пошло не так")

    with pytest.raises(ValueError):
        fail()

    captured = capsys.readouterr()
    assert captured.out == (
        "fail error: ValueError. Inputs: (), {}\n"
    )


def test_log_type_error(capsys):
    """Ошибка типа (TypeError)."""
    @log()
    def add_numbers(a, b):
        return a + b

    with pytest.raises(TypeError):
        add_numbers("1", 2)

    captured = capsys.readouterr()
    assert "add_numbers error: TypeError." in captured.out


# ============================================================
# Тесты для логирования в файл
# ============================================================

def test_log_success_to_file():
    """Успешное выполнение — запись в файл."""
    with tempfile.NamedTemporaryFile(
        mode="w", delete=False, suffix=".txt"
    ) as f:
        filename = f.name

    try:
        @log(filename=filename)
        def my_function(x, y):
            return x + y

        result = my_function(1, 2)

        with open(filename, encoding="utf-8") as f:
            content = f.read()

        assert result == 3
        assert content == "my_function ok\n"
    finally:
        os.unlink(filename)


def test_log_error_to_file():
    """Ошибка — запись в файл."""
    with tempfile.NamedTemporaryFile(
        mode="w", delete=False, suffix=".txt"
    ) as f:
        filename = f.name

    try:
        @log(filename=filename)
        def my_function(x, y):
            return x / y

        with pytest.raises(ZeroDivisionError):
            my_function(1, 0)

        with open(filename, encoding="utf-8") as f:
            content = f.read()

        assert content == (
            "my_function error: ZeroDivisionError. "
            "Inputs: (1, 0), {}\n"
        )
    finally:
        os.unlink(filename)


def test_log_appends_to_file():
    """Логи дописываются в файл (не перезаписываются)."""
    with tempfile.NamedTemporaryFile(
        mode="w", delete=False, suffix=".txt"
    ) as f:
        filename = f.name

    try:
        @log(filename=filename)
        def my_function(x):
            return x * 2

        my_function(1)
        my_function(2)
        my_function(3)

        with open(filename, encoding="utf-8") as f:
            lines = f.readlines()

        assert len(lines) == 3
        assert all(line == "my_function ok\n" for line in lines)
    finally:
        os.unlink(filename)


# ============================================================
# Тесты для метаданных функции
# ============================================================

def test_log_preserves_name():
    """Декоратор сохраняет __name__ функции."""
    @log()
    def my_function():
        return "test"

    assert my_function.__name__ == "my_function"


def test_log_preserves_docstring():
    """Декоратор сохраняет __doc__ функции."""
    @log()
    def my_function():
        """Документация функции."""
        return "test"

    assert my_function.__doc__ == "Документация функции."


# ============================================================
# Тесты для проброса исключений
# ============================================================

def test_log_reraises_exception():
    """Исключение пробрасывается наружу."""
    @log()
    def fail():
        raise RuntimeError("Ошибка")

    with pytest.raises(RuntimeError, match="Ошибка"):
        fail()


def test_log_exception_type_preserved():
    """Тип исключения не меняется."""
    @log()
    def fail():
        raise KeyError("missing")

    with pytest.raises(KeyError):
        fail()
