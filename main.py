from functools import reduce


# Пример с кешированием
@timeit
@slowit(2)
def product(n):
    return reduce(lambda x, y: x * y, range(1, n+1)) if n > 0 else None


# Пример с генератором Фибоначчи
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    # Проверка кеширования
    product(10)
    product(10)

    # Проверка генератора
    f = fibonacci()
    for i in range(10):
        print(next(f))
