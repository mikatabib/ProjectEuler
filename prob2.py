def sum_even_fib(limit=4_000_000):
    total = 0
    a, b = 1, 2
    while a <= limit:
        if not (a & 1):
            total += a
        a, b = b, a+b
    return total
