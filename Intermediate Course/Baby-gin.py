nums = list(map(int, input().split()))
nums_sorted = sorted(nums)

if nums_sorted[0] == nums_sorted[1] == nums_sorted[2]:
    if nums_sorted[3] == nums_sorted[4] == nums_sorted[5] or nums_sorted[3] + 2 == nums_sorted[4] + 1 == \
            nums_sorted[5]:
        print("Baby-git")
elif (nums_sorted[0] + 1 == nums_sorted[1] + 1 == nums_sorted[2] == nums_sorted[3]
      == nums_sorted[4] - 1 == nums_sorted[5] - 1):
    print("Baby-git")
elif (nums_sorted[0] + 2 == nums_sorted[1] + 1 == nums_sorted[2] + 1 == nums_sorted[3]
      == nums_sorted[4] == nums_sorted[5] - 1):
    print("Baby-git")
elif (nums_sorted[0] + 2 == nums_sorted[1] + 1 == nums_sorted[2] == nums_sorted[3]
      == nums_sorted[4] - 1 == nums_sorted[5] - 2):
    print("Baby-git")
elif (nums_sorted[0] + 2 == nums_sorted[1] + 1 == nums_sorted[2] and nums_sorted[3] + 2 == nums_sorted[4] + 1 ==
      nums_sorted[5]):
    print("Baby-git")
else:
    print("None")
