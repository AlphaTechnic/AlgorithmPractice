T = int(input())
sum_list = []

for i in range(T):
    N = int(input())
    num_list = []

    for k in range(1, (N + 1)):
        if k % 2 == 0:
            a = k * (-1)
            num_list.append(a)
        else:
            num_list.append(k)
    sum_list.append(sum(num_list))

for index, case in enumerate(sum_list):
    print('#%s' % (index + 1), case)
