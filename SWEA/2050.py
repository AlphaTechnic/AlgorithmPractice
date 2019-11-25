cap_alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                     'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                     'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

input_alphabet = list(input())

for alphabet in input_alphabet:
    if alphabet in cap_alphabet_list:
        print((cap_alphabet_list.index(alphabet)+1), end=' ')
