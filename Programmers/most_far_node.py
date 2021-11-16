# https://programmers.co.kr/learn/courses/30/lessons/49189

def solution(n, edge):
    answer = 0

    graph = [[] for _ in range(n+1)]

    for e in edge:
        start,end = e[0],e[1]

        graph[start].append(end)
        graph[end].append(start)

    queue = []
    distance = [0 for _ in range(n+1)]
    queue.append([1,0])

    distance[1] = -1

    while queue:
        cur = queue.pop(0)

        for i in graph[cur[0]]:
            if distance[i] == 0:
                queue.append([i,cur[1]+1])
                distance[i] = cur[1]+1

    Max = max(distance)

    answer = distance.count(Max)

    return answer