T = int(input())
total_profit_list = []

for i in range(T):
    N = int(input())
    price_list = list(map(int, input().split()))
    profit_list = []

    while price_list:
        max_val = max(price_list)
        max_val_index = price_list.index(max_val)
        buy_price = 0

        for a in price_list[:max_val_index]:
            buy_price += a

        profit = max_val * max_val_index - buy_price
        profit_list.append(profit)
        del price_list[:max_val_index + 1]

    total_profit = 0
    for _ in profit_list:
        total_profit += _
    total_profit_list.append(total_profit)

for index, case in enumerate(total_profit_list):
    print("#%s" % (index + 1), case)
