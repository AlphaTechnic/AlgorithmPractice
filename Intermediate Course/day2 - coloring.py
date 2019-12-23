T = int(input())

k = 0
field = []
while k <= 90:
    line = [i for i in range(k, k + 10)]
    field.append(line)
    k += 10  # // 필드생성

for l in range(T):
    N = int(input())
    coloring_areas = []

    for j in range(N):
        info = list(map(int, input().split()))
        coloring_areas.append(info)  # // 정보입력받음

    red_list = []
    blue_list = []

    for coloring_area in coloring_areas:
        if coloring_area[4] == 1:
            p = coloring_area[0]
            q = coloring_area[1]
            r = coloring_area[2]
            s = coloring_area[3]
            for a in range(p, r + 1):
                for b in range(q, s + 1):
                    red_list.append(field[a][b])

        elif coloring_area[4] == 2:
            p = coloring_area[0]
            q = coloring_area[1]
            r = coloring_area[2]
            s = coloring_area[3]
            for a in range(p, r + 1):
                for b in range(q, s + 1):
                    blue_list.append(field[a][b])

    purple_list = list(set(red_list) & set(blue_list))

    print('#%s' % (l + 1), len(purple_list))
