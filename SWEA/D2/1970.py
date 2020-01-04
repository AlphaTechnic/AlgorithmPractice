T = int(input())
for t in range(T):

    N = int(input())

    count_50000 = int(N / 50000)
    N = N - 50000 * count_50000

    count_10000 = int(N / 10000)
    N = N - 10000 * count_10000

    count_5000 = int(N / 5000)
    N = N - 5000 * count_5000

    count_1000 = int(N / 1000)
    N = N - 1000 * count_1000

    count_500 = int(N / 500)
    N = N - 500 * count_500

    count_100 = int(N / 100)
    N = N - 100 * count_100

    count_50 = int(N / 50)
    N = N - 50 * count_50

    count_10 = int(N / 10)
    N = N - 10 * count_10

    money_list = [count_50000, count_10000, count_5000, count_1000, count_500, count_100, count_50, count_10]

    print("#%s" % (t + 1))

    for money in money_list:
        print(money, end=' ')
    print('')
