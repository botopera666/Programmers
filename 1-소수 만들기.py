def solution(nums):
    import math
    answer=0
    case=[]

    nums=sorted(nums)

    def generate(list, case):
        print(type(list), list)
        if len(list)==3:
            case.append(list)
            print(list)
            return

        case.append(nums[3])
        generate(4, case)
        case.pop()
        generate(4, case)

    generate(nums, case)


    for n in case:
        n=sum(n)
        for i in (2, int(math.sqrt(n))+1):
            if (n%i==0):
                break
        answer+=1

    return answer

'''
24의 약수 1, 2, 3, 4, 6, 8, 12, 24
제곱근 이하의 숫자 중 1 이외의 약수가 없으면 소수 
'''

print(solution([1, 2, 3]))
print(solution([1, 7, 3]))
print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))