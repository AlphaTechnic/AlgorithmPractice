T = int(input())
for t in range(T):
    str1 = input()
    str2 = input()

    if str1 in str2:
        print("#%s" % (t + 1), '1')
    else:
        print("#%s" % (t + 1), '0')
