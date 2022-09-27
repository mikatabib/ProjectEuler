def gcd(m, n):
    while m != 0:
        n, m = m, n % m
    return n

def lcm(m, n):
    return m * n // gcd(m, n)

def main():
    div = 2
    for it in range(2, 21):
        div = lcm(div, it)
    print(div)

main()

