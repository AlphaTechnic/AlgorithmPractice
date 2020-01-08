T = int(input())
for t in range(T):
    N = int(input())
    case = list(map(int, input().split()))
    case_sorted = sorted(case)

    print("#%s" % (t + 1), end=' ')
    for num in case_sorted:
        print(num, end=' ')
    print('')
