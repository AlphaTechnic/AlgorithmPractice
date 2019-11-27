case = list(map(int, input().split()))

if case == [2, 1] or case == [3, 2] or case == [1, 3]:
    print("A")
elif case == [1, 2] or case == [2, 3] or case == [3, 1]:
    print("B")
