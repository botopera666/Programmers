def solution(lottos, win_nums):
    count_0 = lottos.count(0) #알아볼 수 없는 번호 수
    count_match = 0 #일치하는 번호 수

    for i in lottos:
        if i in win_nums:
            count_match += 1

    if count_match>=2:
        lowest_rank=7-count_match
    else: # count_match==1, 0
        lowest_rank=6

    highest_match=count_0+count_match

    if highest_match>=2:
        highest_rank=7-highest_match
    else: # count_match==1, 0
        highest_rank=6

    answer = [highest_rank, lowest_rank]

    return answer

print(solution([1, 2, 3, 4, 0, 0], [1, 2, 30, 40, 31, 41]))
print(solution([1, 2, 3, 0, 0, 0], [1, 2, 30, 40, 31, 41]))
print(solution([0, 0, 0, 0, 0, 0], [1, 2, 30, 40, 31, 41]))
print(solution([1, 2, 30, 40, 31, 41], [1, 2, 30, 40, 31, 41]))

'''

def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
'''

'''
def solution(lottos, win_nums):
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], 
    rank[len(set(lottos) & set(win_nums))]]
    
    # (set(lottos) & set(win_nums))-->교집합(ans)
    
'''

'''
def solution(lottos, win_nums):
    a= [x for x in lottos if x in win_nums] # 일치하는 숫자의 리스트-리스트 내포
    max = lottos.count(0)+len(a)
    min = len(a)

    max = 7- max if max >=1 else 6
    min = 7- min if min >=1 else 6
    return [max,min]
    
리스트 명 = [표현식 for 변수 in 반복 가능한 대상 if 조건문]
삼항 연산자-
a = b if (~) else c

'''

aa=0
bb=1 if aa==0 else aa
print(f'{aa=} {bb=}')