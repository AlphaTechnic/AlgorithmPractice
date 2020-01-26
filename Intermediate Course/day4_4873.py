T = int(input())
for t in range(T):
    L = []

    for i in input():
        L.append(i)

    test = L[0]
    newL = [L[0]]

    while 1:
        for i in range(1, len(L)):
            if L[i] != test:
                newL.append(L[i])
                test = L[i]
            else:
                newL.pop()
                test = '_'
        if L == newL:
            break
        else:
            L = newL
            if len(L) == 0:
                break
            else:
                newL = [L[0]]
                test = L[0]

    print("#%s" % (t + 1), len(L))
