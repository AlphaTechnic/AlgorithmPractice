T = int(input())
data = []
for _ in range(T):
    numbers = list(map(int, input().split()))
    data.append(numbers)


def average(numbers):
    average_numbers = sum(numbers) / len(numbers)
    return average_numbers


num = 1
for line in data:
    result = round(average(line))
    print('#%s' % num, result)
    num = num + 1
