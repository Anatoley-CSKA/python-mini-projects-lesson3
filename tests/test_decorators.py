"""Тесты для модуля decorators."""
import os
import tempfile
import pytest
from src.decorators import log


# ============================================================
# Тесты для логирования в консоль
# ============================================================

def test_log_success_console(capsys):
    """Успешный вызов — вывод в консоль."""
    @log()
    def add(a, b):
        return a + b

    result = add(2, 3)
    captured = capsys.readouterr()
    assert result == 5
    assert "add(2, 3) -> 5" in captured.out


def test_log_error_console(capsys):
    """Вызов с ошибкой — вывод в консоль."""
    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()
    assert "divide(10, 0) -> ERROR: ZeroDivisionError" in captured.out


def test_log_with_kwargs(capsys):
    """Вызов с именованными аргументами."""
    @log()
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"

    result = greet("Alice", greeting="Hi")
    captured = capsys.readouterr()
    assert result == "Hi, Alice!"
    assert "greet('Alice', greeting='Hi')" in captured.out


# ============================================================
# Тесты для логирования в файл
# ============================================================

def test_log_to_file():
    """Логирование записывается в файл."""
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as f:
        filename = f.name

    try:
        @log(filename=filename)
        def multiply(a, b):
            return a * b

        multiply(3, 4)
        multiply(5, 6)

        with open(filename, encoding="utf-8") as f:
            content = f.read()

        assert "multiply(3, 4) -> 12" in content
        assert "multiply(5, 6) -> 30" in content
    finally:
        os.unlink(filename)


def test_log_to_file_error():
    """Ошибка записывается в файл."""
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as f:
        filename = f.name

    try:
        @log(filename=filename)
        def divide(a, b):
            return a / b

        with pytest.raises(ZeroDivisionError):
            divide(10, 0)

        with open(filename, encoding="utf-8") as f:
            content = f.read()

        assert "divide(10, 0) -> ERROR: ZeroDivisionError" in content
    finally:
        os.unlink(filename)


# ============================================================
# Тесты для сохранения метаданных
# ============================================================

def test_log_preserves_name():
    """Декоратор сохраняет имя функции."""
    @log()
    def my_function():
        return "test"

    assert my_function.__name__ == "my_function"


def test_log_preserves_docstring():
    """Декоратор сохраняет docstring."""
    @log()
    def my_function():
        """Документация."""
        return "test"

    assert my_function.__doc__ == "Документация."


# ============================================================
# Тесты для исключений
# ============================================================

def test_log_reraises_exception():
    """Исключение пробрасывается дальше."""
    @log()
    def fail():
        raise ValueError("Ошибка")

    with pytest.raises(ValueError, match="Ошибка"):
        fail()


def test_log_no_args(capsys):
    """Функция без аргументов."""
    @log()
    def get_value():
        return 42

    result = get_value()
    captured = capsys.readouterr()
    assert result == 42
    assert "get_value() -> 42" in captured.out
