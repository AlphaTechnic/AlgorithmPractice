T = int(input())
for t in range(T):

    table = []
    for i in range(9):
        row = list(map(int, input().split()))
        table.append(row)

    switch = 1
    while switch:
        test1 = []
        for row in table:

            if switch == 0:
                break

            for num in row:
                if num in test1:
                    print("#%s" % (t + 1), end=' ')
                    print('0')
                    switch = 0
                    break
                test1.append(num)
            test1 = []

        if switch == 0:
            break

        test2 = []
        for j in range(9):

            if switch == 0:
                break

            for i in range(9):
                if table[i][j] in test2:
                    print("#%s" % (t + 1), end=' ')
                    print('0')
                    switch = 0
                    break
                else:
                    test2.append(table[i][j])
            test2 = []

        if switch == 0:
            break

        test3 = []
        for u in range(3):
            if switch == 0:
                break

            for v in range(3):

                if switch == 0:
                    break

                for i in range(3):

                    if switch == 0:
                        break

                    for j in range(3):
                        if table[i + 3 * v][j + 3 * u] in test3:
                            print("#%s" % (t + 1), end=' ')
                            print('0')
                            switch = 0
                            break
                        test3.append(table[i + 3 * v][j + 3 * u])
                test3 = []

        if switch == 0:
            break

        print('#%s' % (t + 1), end=' ')
        print('1')
        switch = 0
