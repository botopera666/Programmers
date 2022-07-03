sample=[[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]

print(list(filter(lambda y:y>0, [0, 1, 2, 3, 4])))
print(list(lambda y:y>0, [0, 1, 2, 3, 4]))

print(list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*sample))))

print(list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*sample))))