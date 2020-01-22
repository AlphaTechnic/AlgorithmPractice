T = int(input())
for t in range(T):

    standard = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    checker = []

    N = int(input())
    for i in range(1, 100000000):
        string_num = str(N * i)
        for j in string_num:
            if j in checker:
                continue
            else:
                checker.append(j)
        if len(checker) == len(standard):
            print("#%s" % (t+1), N * i)
            break
