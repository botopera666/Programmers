def solution(board, moves):
    answer = 0
    stack = []

    InuseIndex = [] # 위에서부터 증가
    for i in range(len(board[0])):
        for j in range(len(board)):
            if (board[j][i]):
                InuseIndex.append(j)
                break
        if (len(InuseIndex)==i): # i번에 인형이 없음. i==2인 경우 len(InuseIndex)==3이어야 함
            InuseIndex.append(len(board)) # 참조 가능한 값을 초과

    for i in moves:
        if (InuseIndex[i-1]>=len(board)): # i번에 인형이 없음
            continue

        popNumber = board[InuseIndex[i-1]][i-1]

        if (stack): # 스택에 인형이 1개 이상
            if (popNumber == stack[-1]): # 같은 모양
                stack.pop()
                answer+=2
            else: # 다른 모양
                stack.append(popNumber)
        else: # 스택에 인형이 없음
            stack.append(popNumber)

        InuseIndex[i-1]+=1 # InuseIndex가 가리키는 위치를 바꿈. 숫자를 0으로 바꿀 필요 없음

    return answer

'''
0 0 0 0 0
0 0 1 0 2
0 2 5 0 1
4 2 4 4 2

InuseIndex=[3, 2, 1, 3, 1]

[3][0]
[2][1]
[1][2]
[3][3]
[1][4]

n번에서 pop-
board[InuseIndex[n-1]][n-1]

0 0 0
0 0 3
0 2 1

InuseIndex=[-1, 2, 1]
'''

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],
               [1,5,3,5,1,2,1,4,3,1,2,3,5,4,1,2,3]))

'''
x x x x x
x x o x o
x o o x o
o o o o o
o o o o o

'''


'''

def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop()
                        stacklist.pop()
                        answer += 2     
                break

    return answer
    
간단하지만 느림

'''

'''
def solution(board, moves):
    cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
    
    # cols==[[4, 3], [2, 2, 5], [1, 5, 4, 1], [4, 3], [3, 1, 2, 1]]
    # list(zip(*board))==[(0, 0, 0, 4, 3), (0, 0, 2, 2, 5), (0, 1, 5, 4, 1), (0, 0, 0, 4, 3), (0, 3, 1, 2, 1)]
    # board는 [세로][가로], zip(*board)는 [가로][세로]
    
    list(map(함수, 리스트))
    함수 = lambda x: list(filter(lambda y: y > 0, x))
    리스트 = zip(*board)
    
    lambda y: y>0으로 x에서 0보다 큰 수만 뽑음
    
    lambda 매개변수들: 식1 if 조건식 else 식2
    filter(함수, 반복가능한객체)
    
    x x x x x
    x x o x o
    x o o x o
    o o o o o
    o o o o o
    
    a, s = 0, [0]
    # a는 터진 인형, s는 바구니

    for m in moves:
        if len(cols[m - 1]) > 0: # 집을 인형이 남아있다면
            if (d := cols[m - 1].pop(0)) == (l := s.pop()): # 맨 앞, 맨 뒤
                a += 2
            else:
                s.extend([l, d]) # pop()으로 없앤 인형을 다시 넣음

    return a




a = [1, 2, 3, 4]
n = len(a)
if n > 5:
    print(f"List is too long ({n} elements, expected <= 5)")
-->
a = [1, 2, 3, 4]
if (n := len(a)) > 5:
    print(f"List is too long ({n} elements, expected <= 5)")
    
n을 조건문 안에서 선언하고 값을 대입


>>> a = list(map(str, range(10)))
>>> a
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


https://docs.python.org/ko/3/whatsnew/3.8.html
https://dojang.io/mod/page/view.php?id=2286
https://wikidocs.net/64
'''

sample=[[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]

print(list(filter(lambda y:y>0, [0, 1, 2, 3, 4])))

print(list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*sample))))

'''
zip(*sample)은 이중 리스트
원소에 접근하기 위해서는 대응하는 함수도 이중이어야 함

lambda y:y>0의 경우 대응하는 객체는 일차 리스트

list(filter(lambda y:y>0, [0, 1, 2, 3, 4]))의 결괏값은 일차 리스트

list(map(lambda x: 일차 리스트, 이차 리스트)

'''



