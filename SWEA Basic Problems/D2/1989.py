T = int(input())
bool_list = []

for _ in range(T):
    word = list(input())

    letter_list = []
    for i in word:
        letter_list.append(i)

    word.reverse()

    if letter_list == word:
        bool_list.append(1)
    else:
        bool_list.append(0)

for index, case in enumerate(bool_list):
    print("#%s" % (index + 1), case)
