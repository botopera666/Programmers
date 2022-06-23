def solution(numbers):
    number_list={i for i in range(10)}-set(numbers) # numbers에 중복이 없음
    answer=sum(number_list)

    return answer

print(solution([1,2,3,4,6,7,8,0]))
print(solution([5,8,4,0,6,7,9]))


'''
def solution(numbers):
    return sum(range(10)) - sum(numbers)
'''

'''
solution = lambda x: sum(range(10)) - sum(x)
'''

'''
def solution(numbers):
    return sum([i for i in [1,2,3,4,5,6,7,8,9,0] if i not in numbers])
'''