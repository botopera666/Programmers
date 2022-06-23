def solution(id_list, report, k):
    answer=[0 for i in range(len(id_list))]

    reporter_per_id=dict(zip(id_list, [[] for i in range(len(id_list))]))
    # key: id_list, value: []

    for i in report:
        report_list=i.split()
        reporter_per_id[report_list[1]].append(report_list[0])
        # reporter_per_id[피신고자].append[신고자]
        # key: 피신고자, value: [신고자]

    for i in reporter_per_id: #{피신고자: [신고자]}
        reporter_per_id[i]=list(set(reporter_per_id[i])) # 신고자 중복 정리
        if (len(reporter_per_id[i]) >= k): #신고자 수
            for i in reporter_per_id[i]:
                answer[id_list.index(i)]+=1

    return answer
    # 신고자가 받는 메일

'''
for문: {피신고자: [신고자 리스트]}
for문: 신고자 수가 k 이상인가?
    for문: answer[신고자 인덱스]+=1
'''
print(solution(["muzi", "frodo", "apeach", "neo"],
         ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))

'''
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}
    
    reports: {피신고자: 0}
    리스트*n
    [표현식 for 항목 in 리스트 or 튜플 if 조건문]

    for r in set(report):
        reports[r.split()[1]] += 1
    
    reports[피신고자]+=1
    set()을 사용해 중복 정리
    id(피신고자)마다 신고당한 횟수를 기록

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1
            
    중복 제거-피신고자는 모두 다른 신고자를 가짐
    각각의 신고에서 reports[피신고자]의 값이 k 이상일 경우
    id_list에서 신고자의 인덱스=answer의 인덱스

    return answer

for문: 피신고자가 신고당한 건수
for문: 신고마다 신고자에게 정지 메일을 보낼지 결정
'''

'''
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dictionary = {name: [] for name in id_list}

    for i in set(report):
        dictionary[i.split()[1]].append(i.split()[0])

    for i in dictionary:
        if len(dictionary[i]) >= k: 
            for j in dictionary[i]:
                answer[id_list.index(j)] += 1

    return answer

for문: {피신고자: [신고자 리스트]}
for문: 신고자 수가 k 이상인가?
    for문: answer[신고자 인덱스]+=1
    
'''

'''

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dic_report = {id: [] for id in id_list} # 해당 유저를 신고한 ID
    for i in set(report):
        i = i.split()
        dic_report[i[1]].append(i[0])

    for key, value in dic_report.items():
        if len(value) >= k:
            for j in value:
                answer[id_list.index(j)] += 1

    return answer
    
위의 풀이와 같은 방식-items()를 사용

'''



