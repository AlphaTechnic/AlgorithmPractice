N = int(input())
numbers = []

reverse_numbers = sorted(list(range(N+1)), reverse=True)

for i in reverse_numbers:
    print(i, end=' ')
