T = int(input())
result = []

for _ in range(T):

    N, M = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    sum_list = []

    for i in range(0, N - M + 1):
        total = 0
        for k in nums[i:i + M]:
            total += k
        sum_list.append(total)

    diff_max_min = max(sum_list) - min(sum_list)
    result.append(diff_max_min)

for index, case in enumerate(result):
    print("#%s" % (index + 1), case)
