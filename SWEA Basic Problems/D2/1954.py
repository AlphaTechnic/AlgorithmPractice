T = int(input())
for t in range(T):

    N = int(input())

    table = []
    line = []

    for i in range(N):
        for k in range(N):
            line.append(k)
        table.append(line)
        line = []

    num = 1
    v = 0
    n = N
    while N > 1:
        for i in range(N - 1):
            table[v][i + v] = num
            num += 1
        for i in range(N - 1):
            table[i + v][(n - 1) - v] = num
            num += 1
        for i in range(N - 1):
            table[(n - 1) - v][(n - 1) - i - v] = num
            num += 1
        for i in range(N - 1):
            table[(n - 1) - i - v][v] = num
            num += 1
        N -= 2
        v += 1

    if n % 2 == 1:
        table[int((n - 1) / 2)][int((n - 1) / 2)] = n ** 2

    print("#%s" % (t + 1))
    for case in table:
        for i in case:
            print(i, end=' ')
        print('')
