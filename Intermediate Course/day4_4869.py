T = int(input())
for t in range(T):
    N = int(input())

    a = 1
    b = 3
    c = 0
    count = 0
    ans = []

    while count <= int(N/10) - 3:
        c = 2*a + b
        count += 1

        a = b
        b = c

    print("#%s" % (t+1), c)
