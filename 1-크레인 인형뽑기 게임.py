def solution(board, moves):
    answer = 0
    stack = []

    InuseIndex = [] # 위에서부터 증가
    for i in range(len(board[0])):
        for j in range(len(board)):
            if (board[j][i]):
                InuseIndex.append(j)
                break
        # if (j==len(board)-1):
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
InuseIndex=인형이 있는 행

for: 열
    for: 행
        if: board[행][열] 열 고정, 행을 순회하며 인형이 있는지 탐색
            break->다음 줄 if로 넘어감
        if: 열에 인형이 없는 경우
        (j가 마지막 행을 가리킬 때, InuseIndex에 삽입하지 않아 len(InuseIndex) != i+1일 때)
        참조 가능한 값인 0~len(board)-1을 초과한 len(board) 삽입

for: 인형을 뽑을 열(1~N)
    if: 열의 인형위치가 초과값일 경우(인형이 없음) 다음으로 패스
    
    popNumber=board[행][열] (인형 번호)
    
    if: 스택에 인형이 있다면
        if: 같은 모양
        else: 다른 모양
    else: 스택에 인형이 없다면
    
    InuseIndex[열]+=1
    
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

                if len(stacklist) > 1: #if stacklist
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop()
                        stacklist.pop()
                        answer += 2     
                break

    return answer

for: 인형을 뽑을 열(1~N)
    for: 행
        if: board[행][열]에 인형이 있다면?
            if: 스택에 인형이 2개 이상이라면?
                if: 스택[-1]==스택[-2]라면?
            break 


간단하지만 느림

'''

'''
def solution(board, moves):
    cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
    
    cols==[[4, 3], [2, 2, 5], [1, 5, 4, 1], [4, 3], [3, 1, 2, 1]]
    list(zip(*board))==[(0, 0, 0, 4, 3), (0, 0, 2, 2, 5), (0, 1, 5, 4, 1), (0, 0, 0, 4, 3), (0, 3, 1, 2, 1)]
    board는 [행][열], zip(*board)는 [열][행]
    
    list(map(함수, 리스트))
    함수 = lambda x: list(filter(lambda y: y > 0, x))
    리스트 = zip(*board)
    
    x: zip(*board)의 일차 리스트
    filter(함수, 반복가능한객체)
    lambda y: y>0으로 x에서 0보다 큰 수만 뽑음

    x x x x x
    x x o x o
    x o o x o
    o o o o o
    o o o o o
    
    a, s = 0, [0]

    for m in moves:
        if len(cols[m - 1]) > 0: 
            if (d := cols[m - 1].pop(0)) == (l := s.pop()): 
                a += 2
            else:
                s.extend([l, d]) # pop()으로 없앤 인형을 다시 넣음

    return a

cols=[[4, 3], [2, 2, 5], [1, 5, 4, 1], [4, 3], [3, 1, 2, 1]]
a, s=터진 인형, 스택

for: 인형을 뽑을 열(1~N)
    if: i열의 인형 개수>0 (집을 인형이 남아있는가?)
        if: i열.pop(0)==스택.pop()
            터진 인형+=2
        else: 스택 삽입


def solution(board, moves):
    print(board)
    print(*board)
    print(zip(*board))
    print(list(zip(*board)))
    print(lambda x: list(filter(lambda y: y > 0, x)), zip(*board))
    print(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
    print(list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board))))
    
[[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
[0, 0, 0, 0, 0] [0, 0, 1, 0, 3] [0, 2, 5, 0, 1] [4, 2, 4, 4, 2] [3, 5, 1, 3, 1]
<zip object at 0x000002316F8933C0>
[(0, 0, 0, 4, 3), (0, 0, 2, 2, 5), (0, 1, 5, 4, 1), (0, 0, 0, 4, 3), (0, 3, 1, 2, 1)]
<function solution.<locals>.<lambda> at 0x000002316F886EE0> <zip object at 0x000002316F893400>
<map object at 0x000002316F892D90>
[[4, 3], [2, 2, 5], [1, 5, 4, 1], [4, 3], [3, 1, 2, 1]]

'''

sample=[[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]

print(list(filter(lambda y:y>0, [0, 1, 2, 3, 4])))
print(list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*sample))))

# [1, 2, 3, 4]
# [[4, 3], [2, 2, 5], [1, 5, 4, 1], [4, 3], [3, 1, 2, 1]]
'''
zip(*sample)은 이중 리스트

lambda y:y>0에서 y에 대응하는 객체는 일차 리스트의 원소

list(filter(lambda y:y>0, [0, 1, 2, 3, 4]))의 결괏값은 일차 리스트

list(map(lambda 일차 리스트: list(y>0인 원소), 이차 리스트))
x에 zip(*sample)의 일차 리스트가 대응함

=================================================================
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

