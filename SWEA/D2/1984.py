T = int(input())
result = []

for i in range(T):
    num_list = list(map(int, input().split()))
    max_value = max(num_list)
    min_value = min(num_list)

    list_refined = []
    for k in num_list:
        if k != max_value and k != min_value:
            list_refined.append(k)
        else:
            continue
    average = int(round(sum(list_refined) / len(list_refined)))
    result.append(average)

for index, case in enumerate(result):
    print('#%s' % (index + 1), case)
