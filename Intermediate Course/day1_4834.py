T = int(input())
result = []

for _ in range(T):
    N = int(input())
    cards = list(map(int, list(input())))

    numset_cards = sorted(list(set(cards)), reverse=True)
    counts = []

    for num in numset_cards:
        count = cards.count(num)
        counts.append(count)

    index_max = counts.index(max(counts))

    result.append([numset_cards[index_max], counts[index_max]])

for index, case in enumerate(result):
    print("#%s" % (index + 1), case[0], case[1])
