T = int(input())
for t in range(T):

    N = int(input())

    str_comp_list = []
    str_decomp = []

    for n in range(N):
        str_comp = list(input().split())
        str_comp_list.append(str_comp)

    for i in str_comp_list:
        for j in range(int(i[1])):
            str_decomp.append(i[0])

    print("#%s" % (t+1))
    for index, case in enumerate(str_decomp):
        if index % 10 == 9:
            print(case)
        else:
            print(case, end='')
    print('')
