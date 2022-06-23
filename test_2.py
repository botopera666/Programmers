def solution(n, lost, reserve):
    # 여벌 체육복을 도난당한 학생
    for i in lost[:]:
        if i in reserve:
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
print(solution(10, [2, 4, 6, 3, 1], [1, 3, 5, 8, 7]))