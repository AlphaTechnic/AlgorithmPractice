T = int(input())
for t in range(T):
    N, M = map(int, input().split())

    if N >= M:
        big = N
        small = M
    else:
        big = M
        small = N

    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))

    if len(list1) >= len(list2):
        list_big = list1
        list_small = list2
    else:
        list_big = list2
        list_small = list1

    ans = -1000000

    b = 0
    sum_val = 0
    for _ in range(big - small + 1):
        for a in range(small):
            sum_val += list_small[a] * list_big[a + b]
        b += 1
        if sum_val >= ans:
            ans = sum_val
        sum_val = 0

    print("#%s" % (t + 1), end=' ')
    print(ans)
