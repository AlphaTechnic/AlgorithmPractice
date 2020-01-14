T = int(input())
for t in range(T):
    N = int(input())
    table = []

    for m in range(N):
        nums = list(map(int, input().split()))
        table.append(nums)

    print('#%s' % (t + 1))

    a = 0
    b = 0
    c = 0
    while c < N:
        for i in range(N):
            print(table[N - 1 - i][a], end='')
            if i == N - 1:
                print('', end=' ')
        a += 1

        for j in range(N - 1, -1, -1):
            print(table[N - 1 - b][j], end='')
            if j == 0:
                print('', end=' ')
        b += 1

        for k in range(N):
            print(table[k][N - 1 - c], end='')
            if k == N - 1:
                print('')
        c += 1
