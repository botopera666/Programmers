def solution(answer):
    import re
    # 1
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    return answer



print(solution("."))


