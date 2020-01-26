T = int(input())
for t in range(T):
    N = int(input())
    numlist = sorted(list(map(int, input().split())), reverse=True)
    sorted_list = []

    if len(numlist) % 2 == 0:
        while len(numlist) != 0:
            sorted_list.append(numlist[0])
            numlist.remove(numlist[0])
            sorted_list.append(numlist[len(numlist) - 1])
            numlist.remove(numlist[len(numlist) - 1])

        print("#%s" % (t + 1), end=' ')
        for num in sorted_list[:10]:
            print(num, end=' ')
        print()

    if len(numlist) % 2 == 1:
        while len(numlist) != 1:
            sorted_list.append(numlist[0])
            numlist.remove(numlist[0])
            sorted_list.append(numlist[len(numlist) - 1])
            numlist.remove(numlist[len(numlist) - 1])
        sorted_list.append(numlist[0])

        print("#%s" % (t + 1), end=' ')
        for num in sorted_list[:10]:
            print(num, end=' ')
        print()
