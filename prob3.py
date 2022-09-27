def gpf(n):
    it = 2
    m = float('-inf')
    while it * it <= n:
        if n % it:
            it += 1
        else:
            n //= it
            m = max(m, it)
    m = max(m, n)
    return m
