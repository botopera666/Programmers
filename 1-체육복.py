def solution(n, lost, reserve):
    lost.sort()

    # 여벌 체육복을 도난당한 학생
    for i in lost[:]:
        if i in reserve:
            print(i)
            reserve.remove(i)
            lost.remove(i)

    # i-1, i+1이 모두 reserve일 경우 i-1부터
    for i in lost[:]:
        if (i-1 in reserve):
            reserve.remove(i-1)
            lost.remove(i)
            continue
        if (i+1 in reserve):
            reserve.remove(i+1)
            lost.remove(i)

    return n-len(lost)

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))


'''
for문을 쓰며 요소를 제거하면 인덱스가 밀리므로 리스트를 복사([:])하여 사용

lost=[2, 4]
reserve=[1, 3]
2가 3을 가지면 4는 입을 것이 없으므로 2가 1을 가지는 것이 좋음

'''