T = int(input())

for i in range(T):
    N = int(input())
    nums = list(map(int, input().split()))

    max_value = 0
    min_value = 1000000
    for k in nums:
        if k > max_value:
            max_value = k
        if k < min_value:
            min_value = k

    print("#%s" % (i + 1), max_value - min_value)
