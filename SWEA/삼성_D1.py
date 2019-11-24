T = int(input())
data = []
for _ in range(T):
    num = input().split()
    map_num = map(int, num)
    list_num = list(map_num)
    data.append(list_num)

sum_list = []
for i in data:
    line = []
    for k in i:
        if k % 2 == 1:
            line.append(k)
        else:
            continue
    sum_list.append(line)

for i in range(T):
    a = sum(sum_list[i])
    print('#%s' % (i + 1), a)
