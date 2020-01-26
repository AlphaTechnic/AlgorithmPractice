T = int(input())
result = []

for _ in range(T):
    K, N, M = tuple(map(int, input().split()))
    charge_index = list(map(int, input().split()))

    charges = []
    for i in range(N):
        if i in charge_index:
            charges.append(1)
        else:
            charges.append(0)

    charge_point = 0
    count = 0

    while charge_point < N - K:
        check = False
        for i in range(charge_point + K, charge_point, -1):
            if charges[i] == 1:
                count += 1
                charge_point = i
                check = True
                break
        if not check:
            count = 0
            charge_point = N - K
            break

    result.append(count)

for index, case in enumerate(result):
    print("#%s" % (index + 1), case)
