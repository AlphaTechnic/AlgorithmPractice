T = int(input())
pair_num_list = []
for _ in range(T):
    pair_num = list(map(int, input().split()))
    pair_num_list.append(pair_num)

for index, case in enumerate(pair_num_list):
    print('#%s' % (index + 1), case[0] // case[1], case[0] % case[1])
