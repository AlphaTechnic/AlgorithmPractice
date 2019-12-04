small_alphabet_set = list("abcdefghijklmnopqrstuvwxyz")
cap_alphabet_set = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

input_alphabet = list(input())

for a in input_alphabet:
    if a in small_alphabet_set:
        alphabet_index = small_alphabet_set.index(a)
        print(cap_alphabet_set[alphabet_index], end='')
    else:
        print(a, end='')
