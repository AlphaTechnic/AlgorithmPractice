T = int(input())
for t in range(T):

    N = int(input())

    print("#%s" % (t + 1), end=' ')

    primes = [2, 3, 5, 7, 11]
    count = 0
    for num in primes:
        for i in range(1, 10000):
            if N % num ** i == 0:
                count += 1
            else:
                break

        if num == 11:
            print(count)
        else:
            print(count, end=' ')

        count = 0
