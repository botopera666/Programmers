def solution(answers):
    correct_1=0
    correct_2=0
    correct_3=0

    for i in range(len(answers)):
        # i 인덱스에서 1, 2, 3번 수포자의 답
        answer_1=(i%5)+1
        answer_2=2 if (i%2)==0 else 1 if ((i//2)%4 == 0) else ((i//2)%4)+2

        temp=(i//2)%5
        if (temp==0):
            answer_3=3
        elif (temp==1):
            answer_3=1
        elif (temp==2):
            answer_3=2
        elif (temp==3):
            answer_3=4
        else:
            answer_3=5

        # 1, 2, 3번 수포자의 답과 answer가 일치하는가?
        answer=answers[i]
        if answer==answer_1: correct_1+=1
        if answer==answer_2: correct_2+=1
        if answer==answer_3: correct_3+=1

    # 가장 문제를 많이 맞힌 사람
    renouncer=[]
    correct=[correct_1, correct_2, correct_3]
    high_score=max(correct)
    for i in range(3):
        if (correct[i] == high_score):
            renouncer.append(i+1)

    return renouncer


print(solution([1, 2, 3, 4 ,5]))
print(solution([1, 3, 2, 4, 2]))

'''
1번
(인덱스%5)+1

2번
(인덱스%2)==0이면 2
(인덱스%2)!=0이면
    ((인덱스//2)%4)==0일 때 1
    ((인덱스//2)%4)!=0일 때 ((인덱스//2)%4)+2

3번
((인덱스//2))%5)의 값이 (혹은 (int)(인덱스/2))
0이면 3
1이면 1
2이면 2
3이면 4
4이면 5

요소의 모든 인덱스
https://www.delftstack.com/ko/howto/python/find-all-indices-of-element-in-list-python/
'''
