# https://programmers.co.kr/learn/courses/30/lessons/43162

def search(i, arr, check):
    check[i] = True

    for num in arr[i]:
        if not check[num]:
            search(num,arr,check)
        else:
            continue

def solution(n, computers):
    answer = 0
    
    print('fe')

    graph = []

    for i in range(n):
        l = []
        for j in range(n):
            if i != j and computers[i][j] == 1:
                l.append(j)
        graph.append(l)

    check = [False for _ in range(n)]

    for i in range(n):
        if not check[i]:
            answer+=1
            search(i,graph,check)


    return answer