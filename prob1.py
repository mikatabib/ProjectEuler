def main():
    # arimathic sequence
    # 1/2 * n * (a + Un)
    func = lambda a, n, un: .5 * n * (a + un)

    s3 = int(func(3, LIM//3,  LIM-LIM%3))
    s5 = int(func(5, LIM//5, LIM-LIM%5))
    s15 = int(func(15, LIM//15, LIM-LIM%15))

    num = s3+s5-s15
    print(num)

main()
