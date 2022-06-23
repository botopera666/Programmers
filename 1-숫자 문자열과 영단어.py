def solution(s):
    import re

    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    match_dict = dict(zip(words, numbers))

    for i in words:
        if (s.isdigit()):  # 없어도 되는 코드
            break
        s = re.sub(i, match_dict[i], s)

    answer = int(s)
    return answer


print(solution('one34zerotwo'))
print(solution('1234'))
print(solution('zeroonefivesix'))

'''
num_dic = {
    "zero":"0", 
    "one":"1", 
    "two":"2", 
    "three":"3", 
    "four":"4", 
    "five":"5", 
    "six":"6", 
    "seven":"7", 
    "eight":"8", 
    "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
'''

'''
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)

    인덱스 사용-
    words[0]=='zero'
    str(i)=='0'
'''