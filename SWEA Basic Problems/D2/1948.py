T = int(input())
for t in range(T):

    month_31 = [1, 3, 5, 7, 8, 10, 12]
    month_30 = [4, 6, 9, 11]
    month_28 = [2]

    month1, day1, month2, day2 = map(int, input().split())

    ans = 0
    for i in range(month1, month2 + 1):
        if i in month_31:
            ans += 31
            if i == month1:
                ans -= day1-1
            if i == month2:
                ans -= 31-day2
        elif i in month_30:
            ans += 30
            if i == month1:
                ans -= day1-1
            if i == month2:
                ans -= 30-day2
        elif i in month_28:
            ans += 28
            if i == month1:
                ans -= day1-1
            if i == month2:
                ans -= 28-day2

    print("#%s" % (t+1), ans)
