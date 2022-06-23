def solution(n):
    str_n = ''
    while n:
        n, temp=divmod(n, 3)
        str_n+=str(temp)
    # n=n//3
    # temp=n%3
    # str_n=str_n[::-1] 결과가 역순이므로 뒤집지 않고 그대로 둠

    answer=int(str_n, 3) # 10진수로 변환
    return answer

print(solution(45))
print(solution(125))

'''
def solution(n):
    str_n = ''
    while n:
        n=n//3
        str_n += str(n % 3)
    print(str_n)

    str_n=str_n[::-1]
    answer=int(str_n, 3)
    
    
while 45:
    str_n+=str(0)
    n=15

while 15:
    str_n+=str(0)
    n=5

while 5:
    str_n+=str(2)
    n=1

while 1:
    str_n+=str(1)
    n=0


9진법까지 가능함

while 1351:
    tmp+=str(1351 % 10) ->1
    n=n//10 ->135

while 135:
    ...

while 13:
    tmp+=str(13 % 10) ->3
    n=n//10 ->1

while 1:
    tmp+=str(1 % 10) ->1
    n=n//10 ->0

'''