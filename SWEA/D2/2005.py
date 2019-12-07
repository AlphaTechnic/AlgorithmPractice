T = int(input())
for i in range(T):
    N = int(input())
    line1 = [1]
    line2 = [1, 1]


    def line_created(n):
        line_n = []
        if n == 1:
            return line1
        elif n == 2:
            return line2
        else:
            for num in range(n):
                if num == 0 or num == n - 1:
                    line_n.append(1)
                else:
                    line_n.append(line_created(n - 1)[num - 1] + line_created(n - 1)[num])
            return line_n


    print('#%s' % (i + 1))
    for a in range(N):
        line = line_created(a + 1)
        for index in line:
            print(index, end=' ')
        print('')
