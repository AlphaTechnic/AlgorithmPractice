T = int(input())
for t in range(T):
    time = list(map(int, input().split()))
    hour = time[0] + time[2]
    minute = time[1] + time[3]

    if minute >= 60:
        minute = minute - 60
        hour = hour + 1
    if hour >= 12:
        hour = hour - 12

    print("#%s" % (t+1), hour, minute)
