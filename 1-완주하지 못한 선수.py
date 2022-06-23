def solution(participant, completion):
    set_participant=set(participant)
    set_completion=set(completion)
    if (difference_set:=set_participant-set_completion): # 동명이인 없음 or 동명이인이 있지만 타인이 미완주자
        return "".join(difference_set)
    else: # 동명이인이 미완주자
        for i in set_completion:
            participant.remove(i)
        if (set(participant)==1): # 동명이인 한 명만 남았을 때
            return "".join(participant)
        else: # 각각 다른 이름의 동명이인

'''
participant=aabbbc {a, b, c}
completion=abbbc {a, b, c}


'''


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

'''
import collections
def solution(par,comp):
    return list(collections.Counter(par)-collections.Counter(comp))[0]
'''