import math

def reverse_number(n: int):
    digit = int(math.log10(n))
    rev = 0
    for it in range(digit, -1, -1):
        rev += (n % 10) * 10 ** it
        n //= 10
    return rev


def main():
    m = float('-inf')
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            n = i * j
            if reverse_number(n) == n:
                m = max(n, m)
    print(m)


main()
