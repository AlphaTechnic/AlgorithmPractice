T = int(input())
for t in range(T):
    string = list(input())
    ans = []

    for char in string:
        if ans == []:
            ans.append(char)
            continue
        if char == ans[-1]:
            ans.pop(-1)
        elif char != ans[-1]:
            ans.append(char)

    print("#%s" % (t+1), len(ans))
