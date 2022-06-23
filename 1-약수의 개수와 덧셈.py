def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        square_root=i**(1/2) # 혹은 math.sqrt() 사용
        if (square_root == int(square_root)): # 실수
            answer+=i
        else: # 정수
            answer-=i
    return answer

'''
16의 제곱근 4
16의 약수 1, 2, 4, 8, 16

제곱근이 정수인 경우 약수의 개수는 홀수

30의 제곱근 5.x
30의 약수 1, 2, 3, 5, 6, 10, 15, 30

제곱근이 실수인 경우 약수의 개수는 짝수
'''