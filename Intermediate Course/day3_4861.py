T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    str_map = []

    for n in range(N):
        letters = list(input())
        str_map.append(letters)

    word = []
    for letters in str_map:
        for i in range((M - 1), N):
            for letter in letters[i - M + 1: i + 1]:
                word.append(letter)
            if word == list(reversed(word)):
                print("#%s" % (t + 1), end=' ')
                for result in word:
                    print(result, end='')
                print()
            else:
                word = []

    str_map_transposed = [list(x) for x in zip(*str_map)]
    for letters in str_map_transposed:
        for i in range((M - 1), N):
            for letter in letters[i - M + 1: i + 1]:
                word.append(letter)
            if word == list(reversed(word)):
                print("#%s" % (t + 1), end=' ')
                for result in word:
                    print(result, end='')
                print()
            else:
                word = []
