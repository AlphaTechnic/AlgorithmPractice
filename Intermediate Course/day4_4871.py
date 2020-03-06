T = int(input())
for t in range(T):

    ###### graph 만들기
    graph = {}

    V, E = map(int, input().split())

    for i in range(E):
        first, sec = map(int, input().split())
        if first not in graph:
            graph[first] = {sec}
        else:
            graph[first].add(sec)
    for k in range(1, V + 1):
        if k not in graph:
            graph[k] = {}

    ###### dfs 함수 만들기 - 경로가 존재하면 global변수 a를 1로 바꿈
    a = 0

    def dfs(graph, start, end, visited=[]):
        visited += [start]

        if start == end:
            global a
            a = 1

        for node in graph[start]:
            if node not in visited:
                dfs(graph, node, end, visited)

    start, end = map(int, input().split())

    dfs(graph, start, end)

    print("#%s" % (t + 1), a)
