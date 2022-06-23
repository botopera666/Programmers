def solution(absolutes, signs):

    original=[absolutes[i] if signs[i] else -absolutes[i] for i in range(len(absolutes))]
    return sum(original)

print(solution([4, 7, 12], [True, False, True]))

'''
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))

print(list(zip(absolutes, signs)))-->[(4, True), (7, False), (12, True)]
'''