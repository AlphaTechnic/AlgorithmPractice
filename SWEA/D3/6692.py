T = int(input())
for t in range(T):
    ans = 0
    N = int(input())
    for n in range(N):
        p, x = map(float, input().split())
        ans += p*x

    print("#%s" % (t + 1), round(ans, 6))
