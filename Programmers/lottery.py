# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    ans = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6,0:6}

    hits = 0
    num_zero = 0

    for l in lottos:
        if l != 0 and l in win_nums:
            hits += 1
        elif l == 0:
            num_zero += 1

    most, least = 0, 0

    if hits == 6:
        return [1,1]
    else:
        least = hits
        most = hits + num_zero

    print(most, least)

    answer = [ans[most], ans[least]]

    return answer