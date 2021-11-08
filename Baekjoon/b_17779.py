import copy

n = int(input())

city = [[0]* (n+1) for _ in range(n+1)]

def arr_print(arr):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(arr[i][j],end= ' ')
        print()
    print()

for i in range(n):
    l = list(map(int, input().split()))
    for j in range(n):
        city[i+1][j+1] = l[j]

def check(x, y, d1, d2):
    if d1 >=1 and d2 >=1 and x < x + d1 + d2 <= n and 1 <= y-d1 < y < y+ d2 <=n:
        return True

    return False

def line1(arr, x, y, d1, d2):
    for i in range(d1+1):
        arr[x+i][y-i] = 5

    return arr

def line2(arr, x, y, d1, d2):
    for i in range(d2+1):
        arr[x+i][y+i] = 5

    return arr

def line3(arr, x, y, d1, d2):
    for i in range(d2+1):
        arr[x+d1+i][y-d1+i] = 5

    return arr

def line4(arr, x, y, d1, d2):
    for i in range(d1+1):
        arr[x+d2+i][y+d2-i] = 5

    return arr

def divide_area(arr, x, y, d1, d2):
    for r in range(1, n+1):
        for c in range(1, n+1):
            if arr[r][c] == 5:
                break
            else:
                if 1<= r < x+d1 and 1<= c <= y:
                    arr[r][c] = 1
                elif 1<= r <= x+d2 and y < c <= n:
                    arr[r][c] = 2
                elif x+d1 <= r <= n and 1 <=c < y-d1+d2:
                    arr[r][c] = 3
                elif x+d2 < r <=n and y-d1-d2 <= c <= n:
                    arr[r][c] = 4
                else:
                    arr[r][c] = 5

    for r in range(n, 0, -1):
        for c in range(n, 0, -1):
            if arr[r][c] == 5:
                break
            else:
                if 1<= r < x+d1 and 1<= c <= y:
                    arr[r][c] = 1
                elif 1<= r <= x+d2 and y < c <= n:
                    arr[r][c] = 2
                elif x+d1 <= r <= n and 1 <=c < y-d1+d2:
                    arr[r][c] = 3
                elif x+d2 < r <=n and y-d1-d2 <= c <= n:
                    arr[r][c] = 4
                else:
                    arr[r][c] = 5
    for r in range(1, n+1):
        for c in range(1, n+1):
            if arr[r][c] == 0:
                arr[r][c] = 5

    return arr

"""x,y,d1,d2 = 4,3,1,1

arr_print(line1(temp, x, y, d1, d2))
arr_print(line2(temp, x, y, d1, d2))
arr_print(line3(temp, x, y, d1, d2))
arr_print(line4(temp, x, y, d1, d2))

arr_print(divide_area(temp, x, y, d1, d2))"""

MIN = float('inf')

for x in range(1, n+1):
    for y in range(1, n+1):
        for d1 in range(1, n+1):
            for d2 in range(1, n+1):
                if check(x, y, d1, d2):
                    citizen = [0,0,0,0,0,0]

                    tmp = [[0] * (n + 1) for _ in range(n + 1)]

                    #tmp = copy.deepcopy(city)

                    tmp = line1(tmp, x, y, d1, d2)
                    tmp = line2(tmp, x, y, d1, d2)
                    tmp = line3(tmp, x, y, d1, d2)
                    tmp = line4(tmp, x, y, d1, d2)

                    tmp = divide_area(tmp, x, y, d1, d2)

                    for i in range(1, n+1):
                        for j in range(1, n+1):
                            citizen[tmp[i][j]] +=city[i][j]

                    citizen = citizen[1:]

                    MIN = min(MIN, (max(citizen)-min(citizen)))


print(MIN)
'''
7
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1

'''