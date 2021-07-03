T = int(input())
for t in range(T):
    P, Q, R, S, W = map(int, input().split())

    feeA = P*W
    feeB = 0

    if W <= R:
        feeB = Q
    elif W > R:
        feeB = Q + S*(W-R)

    print("#%s" % (t+1), min(feeA, feeB))
