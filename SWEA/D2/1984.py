T = int(input())
result = []

for i in range(T):
    num_list = list(map(int, input().split()))
    max_vlaue = max(num_list)
    min_value = min(num_list)

    num_list.remove(max_vlaue)
    num_list.remove(min_value)

    average = int(sum(num_list) / len(num_list))
    result.append(average)

for index, case in enumerate(result):
    print('#%s' % (index + 1), case)
