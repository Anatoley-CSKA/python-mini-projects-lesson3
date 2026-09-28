# Без кеширования время работы функции при каждом вызове не менее 2 секун
from functools import reduce


@timeit
@slowit(2)
def product(n):
    return reduce(lambda x, y: x * y, range(1, n+1)) if n > 0 else None

product(10)
product(10)
