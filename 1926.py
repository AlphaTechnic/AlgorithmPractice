N = int(input())
case = list(range(1, (N+1)))


def clap(number_list):
    num_list_str = list(map(str, number_list))

    clear3_list = []
    clear3_6_list = []
    clear3_6_9_list = []
    list_clap = []

    for num in num_list_str:
        a = num.replace('3', '-')
        clear3_list.append(a)
    for num in clear3_list:
        b = num.replace('6', '-')
        clear3_6_list.append(b)
    for num in clear3_6_list:
        c = num.replace('9', '-')
        clear3_6_9_list.append(c)

    for num in clear3_6_9_list:
        k = num.count('-')
        if k == 1:
            num = '-'
        elif k == 2:
            num = '--'
        list_clap.append(num)

    return list_clap


for i in clap(case):
    print(i, end=' ')
