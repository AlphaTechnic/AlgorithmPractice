T = int(input())
for t in range(T):
    _ = input()

    case = [x for x in range(101)]
    count = [0 for x in range(101)]

    scores = list(map(int, input().split()))
    for score in scores:
        count[score] += 1

    count_max = max(count)

    for i in range(100, -1, -1):
        if count[i] == count_max:
            print('#%s' % (t + 1), end=' ')
            print(case[i])
            break
