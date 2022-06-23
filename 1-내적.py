def solution(a, b):
    answer=sum([n1*n2 for n1, n2 in zip(a, b)])
    return answer

print(solution([1, 2, 3, 4], [-3, -1, 0, 2]))

'''
solution = lambda x, y: sum(a*b for a, b in zip(x, y))

'''
