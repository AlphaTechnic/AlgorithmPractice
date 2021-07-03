T = int(input())

for a in range(T):
    N_students, K_th = list(map(int, input().split()))

    scores_list = []
    for i in range(N_students):
        scores = list(map(int, input().split()))
        scores_list.append(scores)

    result = []
    for student in scores_list:
        final_score = student[0] * 0.35 + student[1] * 0.45 + student[2] * 0.2
        result.append(final_score)

    ranked_result = sorted(result, reverse=True)
    x = int(N_students / 10)
    A1_list = ranked_result[:x]
    A2_list = ranked_result[x:(2 * x)]
    A3_list = ranked_result[(2 * x):(3 * x)]
    B1_list = ranked_result[(3 * x):(4 * x)]
    B2_list = ranked_result[(4 * x):(5 * x)]
    B3_list = ranked_result[(5 * x):(6 * x)]
    C1_list = ranked_result[(6 * x):(7 * x)]
    C2_list = ranked_result[(7 * x):(8 * x)]
    C3_list = ranked_result[(8 * x):(9 * x)]
    D2_list = ranked_result[(9 * x):]

    if result[K_th - 1] in A1_list:
        print("#%s" % (a + 1), 'A+')
    if result[K_th - 1] in A2_list:
        print("#%s" % (a + 1), 'A0')
    if result[K_th - 1] in A3_list:
        print("#%s" % (a + 1), 'A-')
    if result[K_th - 1] in B1_list:
        print("#%s" % (a + 1), 'B+')
    if result[K_th - 1] in B2_list:
        print("#%s" % (a + 1), 'B0')
    if result[K_th - 1] in B3_list:
        print("#%s" % (a + 1), 'B-')
    if result[K_th - 1] in C1_list:
        print("#%s" % (a + 1), 'C+')
    if result[K_th - 1] in C2_list:
        print("#%s" % (a + 1), 'C0')
    if result[K_th - 1] in C3_list:
        print("#%s" % (a + 1), 'C-')
    if result[K_th - 1] in D2_list:
        print("#%s" % (a + 1), 'D0')
