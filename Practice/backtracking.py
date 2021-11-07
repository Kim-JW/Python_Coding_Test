def arr_print(arr):
    for i in arr:
        for j in i:
            print(j, end= ' ')
        print()
    print()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

Map = [[0]*6 for _ in range(6)]
v = [[False]*6 for _ in range(6)]

def drop(pos, color):
    global Map

    for i in range(6):
        if Map[i][pos] > 0:
            Map[i-1][pos] = color
            break
    else:
        Map[5][pos] = color

    return Map

def check(i,j, color, cnt):
    global Map
    global v

    print(i, j)
    arr_print(Map)
    arr_print(v)

    if cnt == 3:
        return True
    else:
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if nx < 0 or ny < 0 or nx >= 6 or ny >=6:
                continue

            if not v[nx][ny] and Map[nx][ny] == color:
                v[nx][ny] = True
                check(nx, ny, color, cnt +1)

    return False

def boom(i, j, color):
    global Map
    global v

    Map[i][j] = 0
    v[i][j] = True

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]

        if nx < 0 or ny < 0 or nx >= 6 or ny >= 6:
            continue

        if not v[nx][ny] and Map[nx][ny] == color:
            v[nx][ny] = True
            Map[nx][ny] = 0
            boom(nx, ny, color)

def v_init():
    global v
    for i in range(6):
        for j in range(6):
            v[i][j] = False

def solution(macaron):
    answer = []

    global Map
    global v

    for ma in macaron:
        pos, color = ma[0], ma[1]
        pos -= 1

        drop(pos, color)

        arr_print(Map)

        for i in range(5, -1,-1):
            for j in range(6):
                if Map[i][j] > 0:
                    v_init()
                    if check(i,j,color,1):
                        print('fff')
                        boom(i, j, color)
                        arr_print(Map)
                        exit()

    return answer

m1 = [[1,1],[2,1],[1,2],[3,3],[6,4],[3,1],[3,3],[3,3],[3,4],[2,1]]

print(solution(m1))
