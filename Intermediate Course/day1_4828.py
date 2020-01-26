T = int(input())
result = []

for i in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    result.append(max(nums) - min(nums))

for index, case in enumerate(result):
    print("#%s" % (index+1), case)
