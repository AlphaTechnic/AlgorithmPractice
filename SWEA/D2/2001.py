T = int(input())

for i in range(T):
    N, M = list(map(int, input().split()))
    flies = []
    for _ in range(N):
        flies.append(list(map(int, input().split())))

    flies_rearranged = []

    for t in range(N - M + 1):
        for s in range(N - M + 1):
            for q in range(t, t + M):
                for p in range(s, s + M):
                    flies_rearranged.append(flies[q][p])

    num_dead_flies = []
    for _ in range((N - M + 1) ** 2):
        num_dead_flies.append(sum(flies_rearranged[:M ** 2]))
        flies_rearranged = flies_rearranged[M ** 2:]

    max_value = max(num_dead_flies)
    print("#%s" % (i + 1), max_value)
