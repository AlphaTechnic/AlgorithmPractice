T = int(input())
for t in range(T):
    N, K = map(int, input().split())

    table = []
    for i in range(N):
        nums = list(map(int, input().split()))
        table.append(nums)

    standard1 = []
    standard2 = []
    for i in range(K):
        standard1.append(1)
    standard2 = standard1 + [0]

    count = 0
    checker = []

    for i in range(N):
        for k in range(N):
            if table[i][k] == 1:
                checker.append(1)
            elif table[i][k] == 0:
                checker.append(0)
                if checker == standard2:
                    count += 1
                    checker = []
                else:
                    checker = []
        if checker == standard1:
            count += 1
        checker = []

    table = [list(x) for x in zip(*table)]
    for i in range(N):
        for k in range(N):
            if table[i][k] == 1:
                checker.append(1)
            elif table[i][k] == 0:
                checker.append(0)
                if checker == standard2:
                    count += 1
                    checker = []
                else:
                    checker = []
        if checker == standard1:
            count += 1
        checker = []

    print("#%s" % (t+1), end=' ')
    print(count)
