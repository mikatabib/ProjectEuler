from os import write


def sieve(n):
    n += 1
    field = [True] * n
    primes = []

    for it in range(2, n):
        if field[it]:
            primes.append(it)
            for j in range(it + it, n, it):
                field[j] = False
    return primes


# pick a number for approximated limit
# floor(n/log(n)) = 11.814
n = 140_000

# turns out I got 13.010 primes
primes = sieve(n)
print(primes[10_000])
