import math
v1 = [input() for v2 in range(2)]
v3 = v1[0].split(' ')
v4 = int(v3[0])
v5 = int(v3[1])
v3 = v1[1].split(' ')
v6 = [0] * v4
for v2 in range(len(v3)):
    v6[v2] = int(v3[v2])
if v6 == [0] * v4:
    print(v6)
    exit()
if v5 > math.log(v4):
    print([v4] * v4)
    exit()
for v2 in range(v5):
    v7 = [1] * v4
    for v2, v8 in enumerate(v6):
        for v9 in range(1, v8 + 1):
            if v2 - v9 >= 0:
                v7[v2 - v9] += 1
            if v2 + v9 < v4:
                v7[v2 + v9] += 1
    v6 = v7
    print(v6)
    if v6[0] == v4 & v6[-1] == v4:
        break
