T = int(input())
num = 1
for _ in range(T):
    two_numbers = list(map(int, input().split()))
    if two_numbers[0] > two_numbers[1]:
        print("#%s >" % num)
    elif two_numbers[0] == two_numbers[1]:
        print("#%s =" % num)
    else:
        print("#%s <" % num)
    num = num + 1
