T = int(input())

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = len(A)
subsets_A = []
subset_A = []

for i in range(1 << n):
    for j in range(n):
        if i & (1 << j):
            subset_A.append(A[j])
    subsets_A.append(subset_A)
    subset_A = []

for t in range(T):
    N, K = map(int, input().split())

    lenN_subsets_A = []
    for subset in subsets_A:
        if len(subset) == N:
            lenN_subsets_A.append(subset)

    count = 0
    for lenN_subset in lenN_subsets_A:
        if sum(lenN_subset) == K:
            count += 1

    print("#%s" % (t + 1), count)
