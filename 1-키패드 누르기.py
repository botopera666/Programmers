def solution(numbers, hand):
    answer = ''

    number_position={
        1: [0, 0],
        2: [1, 0],
        3: [2, 0],
        4: [0, 1],
        5: [1, 1],
        6: [2, 1],
        7: [0, 2],
        8: [1, 2],
        9: [2, 2],
        '*': [0, 3],
        0: [1, 3],
        '#': [2, 3]
    }

    left_hand_position=number_position['*']
    right_hand_position=number_position['#']

    if (hand == 'left'):
        for i in numbers:
            position=number_position[i]
            if (i in [3, 6, 9]): # 오른쪽 숫자
                answer+=('R')
                right_hand_position=position
            elif (i in [1, 4, 7]): # 왼쪽 숫자
                answer+=('L')
                left_hand_position=position
            else:
                left_distance=abs(left_hand_position[0]-position[0]) + abs(left_hand_position[1]-position[1])
                right_distance=abs(right_hand_position[0]-position[0]) + abs(right_hand_position[1]-position[1])

                if (left_distance > right_distance): # 오른쪽 손이 가깝다
                    answer+=('R')
                    right_hand_position=position
                else: # 왼쪽 손이 가깝거나 거리가 같다
                    answer+=('L')
                    left_hand_position=position


    else: # (hand == 'right')
        for i in numbers:
            position = number_position[i]
            if (i in [3, 6, 9]):  # 오른쪽 숫자
                answer += ('R')
                right_hand_position = position
            elif (i in [1, 4, 7]):  # 왼쪽 숫자
                answer += ('L')
                left_hand_position = position
            else:
                left_distance=abs(left_hand_position[0]-position[0]) + abs(left_hand_position[1]-position[1])
                right_distance=abs(right_hand_position[0]-position[0]) + abs(right_hand_position[1]-position[1])

                if (left_distance < right_distance):  # 왼쪽 손이 가깝다
                    answer += ('L')
                    left_hand_position = position
                else:  # 오른쪽 손이 가깝거나 거리가 같다
                    answer += ('R')
                    right_hand_position = position

    return answer

'''
if: 오른쪽 숫자인가?
elif: 왼쪽 숫자인가?
else: 중간 숫자
    if: 오른족 손이 가까운가?
    else: 왼쪽 손이 가까운가?
'''

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))


'''
def solution(numbers, hand):
    l = 10
    r = 11
    answer = ""
    p = [[0, 4, 3, 4, 3, 2, 3, 2, 1, 2],
         [4, 0, 1, 2, 0, 2, 3, 0, 3, 4],
         [3, 1, 0, 1, 2, 1, 2, 3, 2, 3],
         [4, 2, 1, 0, 3, 2, 1, 4, 3, 2],
         [3, 0, 2, 3, 0, 1, 2, 0, 2, 3],
         [2, 2, 1, 2, 1, 0, 1, 2, 1, 2],
         [3, 3, 2, 1, 2, 1, 0, 3, 2, 1],
         [2, 0, 3, 4, 0, 2, 3, 0, 1, 2],
         [1, 3, 2, 3, 2, 1, 2, 1, 0, 1],
         [2, 4, 3, 2, 3, 2, 1, 2, 1, 0],
         [1, 0, 4, 5, 0, 3, 4, 0, 2, 3],
         [1, 5, 4, 0, 4, 3, 0, 3, 2, 0]]
    for i in numbers:
        if i in [1, 4, 7]:
            l = i
            answer += "L"
        elif i in [3, 6, 9]:
            r = i
            answer += "R"
        else:
            if p[l][i] < p[r][i]:
                l = i
                answer += "L"
            elif p[l][i] > p[r][i]:
                r = i
                answer += "R"
            elif hand == "left":
                l = i
                answer += "L"
            else:
                r = i
                answer += "R"
    return answer

p=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10(*), 11(#)][0~9까지의 거리]

if: 오른쪽 숫자인가?
elif: 왼쪽 숫자인가?
else: 중간 숫자
    if: 오른족 손이 가까운가?
    elif: 왼쪽 손이 가까운가?
    elif: 거리가 같다면 왼손잡이인가?
    else: 거리가 같다면 오른손잡이인가?

'''