import numpy as np
v1 = int(input())
v2 = list(map(int, input().split(' ')))
v3 = [i for v4 in range(1, v1 + 1, 1)]
v2 = np.array(v2)
v3 = np.array(v3)
v2 -= v3
v5 = sum(abs(v2))
while True:
    v6 = v2 < 0
    v7 = v2 > 0
    v6 = v6 * v2
    v7 = v7 * v2
    if abs(sum(v6)) > abs(sum(v7)):
        v2 += (abs(sum(v6)) - abs(sum(v7))) // v1 + 1
    else:
        v2 -= (abs(sum(v7)) - abs(sum(v6))) // v1 + 1
    if v5 <= sum(abs(v2)):
        break
    else:
        v5 = sum(abs(v2))
print(v5)
