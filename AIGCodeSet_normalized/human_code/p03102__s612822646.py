import numpy as np
v1 = list(map(int, input().split(' ')))
v2 = np.array(list(map(int, input().split(' '))))
v3 = [np.array(list(map(int, input().split(' ')))) for v4 in range(v1[0])]
v5 = []
for v4 in range(v1[0]):
    v5.append(np.dot(v2, v3[v4]) + v1[2] > 0)
print(v5.count(True))
