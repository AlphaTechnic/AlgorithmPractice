T = int(input())
for t in range(T):
    N = int(input())
    s = 0
    v = 0

    for n in range(N):
        command = list(map(int, input().split()))

        if len(command) == 2:
            d = command[0]
            a = command[1]

            if d == 1:
                v += a
                s += v
            elif d == 2:
                if v > a:
                    v -= a
                    s += v
                else:
                    v = 0

        elif len(command) == 1:
            s += v

    print("#%s" % (t + 1), s)
