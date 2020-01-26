T = int(input())

for t in range(T):
    str1 = input()
    str2 = input()

    max_value = 0
    for letter in str1:
        if max_value < str2.count(letter):
            max_value = str2.count(letter)
    print("#%s" % (t + 1), max_value)
