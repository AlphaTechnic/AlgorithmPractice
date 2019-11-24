T = int(input())
data = []

for _ in range(T):
    numbers = list(map(int, input().split()))
    data.append(numbers)

for index, numbers in enumerate(data):
    print("#%s" % (index + 1), max(numbers))



