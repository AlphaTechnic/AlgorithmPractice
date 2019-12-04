T = int(input())
period_list = []

for _ in range(T):
    word = input()
    if word[0] == word[1] == word[2] == word[3] == word[4] == word[5] == word[6] == word[7] == word[8] == word[9] == \
            word[10] == word[11] == word[12] == word[13] == word[14]:
        period_list.append(1)
    elif word[0:2] == word[2:4] == word[4:6] == word[6:8] == word[8:10] == word[10:12] == word[12:14]:
        period_list.append(2)
    elif word[0:3] == word[3:6] == word[6:9] == word[9:12] == word[12:15]:
        period_list.append(3)
    elif word[0:4] == word[4:8] == word[8:12] == word[12:16]:
        period_list.append(4)
    elif word[0:5] == word[5:10] == word[10:15]:
        period_list.append(5)
    elif word[0:6] == word[6:12] == word[12:18]:
        period_list.append(6)
    elif word[0:7] == word[7:14]:
        period_list.append(7)
    elif word[0:8] == word[8:16]:
        period_list.append(8)
    elif word[0:9] == word[9:18]:
        period_list.append(9)
    elif word[0:10] == word[10:20]:
        period_list.append(10)
    elif word[0:11] == word[11:22]:
        period_list.append(11)
    elif word[0:12] == word[12:24]:
        period_list.append(12)
    elif word[0:13] == word[13:26]:
        period_list.append(13)
    elif word[0:14] == word[14:28]:
        period_list.append(14)
    elif word[0:15] == word[15:30]:
        period_list.append(15)

for index, case in enumerate(period_list):
    print("#%s" % (index + 1), case)
