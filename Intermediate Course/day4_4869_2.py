def recur(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    return 2 * recur(n - 2) + recur(n - 1)


T = int(input())
for t in range(T):
    N = int(input())
    k = int(N / 10)

    print("#%s" % (t + 1), recur(k))
