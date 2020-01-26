T = int(input())
for t in range(T):
    P, Pa, Pb = map(int, input().split())
    l, r = 1, P
    c = int((l + r) / 2)

    count_a = 0
    while c != Pa:
        if c < Pa:
            l = c
            c = int((l + r) / 2)
            count_a += 1
        elif c > Pa:
            r = c
            c = int((l + r) / 2)
            count_a += 1

    l, r = 1, P
    c = int((l + r) / 2)

    count_b = 0
    while c != Pb:
        if c < Pb:
            l = c
            c = int((l + r) / 2)
            count_b += 1
        elif c > Pb:
            r = c
            c = int((l + r) / 2)
            count_b += 1

    if count_a < count_b:
        print("#%s" % (t + 1), "A")
    elif count_a > count_b:
        print("#%s" % (t + 1), "B")
    else:
        print("#%s" % (t + 1), '0')
