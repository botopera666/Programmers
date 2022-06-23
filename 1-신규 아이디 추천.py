def solution(new_id):
    import re
    # 1
    new_id = new_id.lower()

    # 2
    # replace는 정규식 패턴을 찾지 못함
    new_id = re.sub('[^a-z0-9._-]', '', new_id)

    # 3
    new_id = re.sub('[.]{1,}', '.', new_id)
    # https: // wikidocs.net / 4308  # mn
    # 문자 .이 1번 이상 반복됨

    # 4
    if (new_id):  # 빈 문자열이 아니라면
        if (new_id[0] == '.'):
            new_id = new_id[1:]
        if (new_id and new_id[-1] == '.'):  # new_id=='.'인 경우-단락 평가
            new_id = new_id[:-1]

    # 5
    if (not new_id):
        new_id = 'a'

    # 6
    if (len(new_id) >= 16):
        new_id = new_id[:15]
        if (new_id[-1] == '.'):
            new_id = new_id[:-1]

    # 7
    while (len(new_id) <= 2):
        new_id += new_id[-1]

    print(new_id)
    return new_id

solution("...!@BaT#*..y.abcdefghijklm")
solution("")
solution("0")
solution(".")
solution("z-+.^.")
solution("=.=")
solution("123_.def")
solution("abcdefghijklmn.p")


'''
import re

def solution(new_id):
    st = new_id 
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
    
    .은 '줄바꿈 문자를 제외한 1글자'를 의미하므로 \. 혹은 [.]이라고 써야 '.'으로 취급
    +: 한 번 이상 반복됨
    ^: 문자열의 맨 앞부터 일치하는 경우 검색
    $: 문자열의 맨 뒤부터 일치하는 경우 검색
    A|B: A 또는 B
    
    [st + "".join([st[-1] for i in range(3-len(st))]
    리스트 내포
    리스트 명 = [표현식 for 변수 in 반복 가능한 대상]
    
    https://velog.io/@ednadev/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D%EA%B3%BC-re%EB%AA%A8%EB%93%88

'''


'''
def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5
    if answer == '':
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer
'''

'''
from re import sub

def solution(new_id):
    new_id = new_id.lower()
    new_id = sub("[^a-z0-9-_.]", "", new_id)
    new_id = sub("\.+", ".", new_id)
    new_id = sub("(^\.|\.$)", "", new_id)
    new_id = new_id if new_id else "a"
    new_id = sub("\.$", "", new_id[:15])
    new_id = new_id if len(new_id) > 3 else new_id + new_id[-1] * (3 - len(new_id))
    return new_id
'''
