# https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''

    keypad = []
    keypad.append([3,1])

    for i in range(3):
        for j in range(3):
            keypad.append([i,j])

    L,R = [3,0],[3,2]

    for n in numbers:
        if n in (1,4,7):
            answer += 'L'
            L = keypad[n]

        elif n in (3,6,9):
            answer += 'R'
            R = keypad[n]

        else:
            n_pos = keypad[n]

            L_dist = abs(L[0]- n_pos[0]) + abs(L[1] - n_pos[1])
            R_dist = abs(R[0]- n_pos[0]) + abs(R[1] - n_pos[1])

            if L_dist < R_dist:
                answer +='L'
                L = keypad[n]
                
            elif L_dist > R_dist:
                answer +='R'
                R = keypad[n]

            else :
                if hand == 'right':
                    answer += 'R'
                    R = keypad[n]
                else:
                    answer += 'L'
                    L = keypad[n]

    return answer