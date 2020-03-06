T = int(input())
for t in range(T):
    stack = []

    string = input()

    check = True
    for i in string:
        if check is False:
            break
        if i == "(" or i == "{":
            stack.append(i)
        elif i == ")" or i == "}":
            if stack == []:
                stack.append("ㅗ")
                check = False
                break
            elif i == ")":
                if stack[-1] == "(":
                    stack.pop(-1)
                else:
                    check = False
                    break
            elif i == "}":
                if stack[-1] == "{":
                    stack.pop(-1)
                else:
                    check = False
                    break

    if stack == []:
        print("#%d" % (t+1), end=' ')
        print("1")
    else:
        print("#%d" % (t+1), end=' ')
        print("0")
