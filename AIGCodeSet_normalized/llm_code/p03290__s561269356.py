from operator import itemgetter
import math
v1, v2 = map(int, input().split())
v3 = [0] * v1
for v4 in range(v1):
    v3[v4] = [0] * 4
    v3[v4][0], v3[v4][1] = map(int, input().split())
    v3[v4][3] = (v4 + 1) * 100
    v3[v4][2] = ((v4 + 1) * 100 * v3[v4][0] + v3[v4][1]) / v3[v4][0]
v5 = 0
v6 = 0
while v6 < v2:
    v3 = sorted(v3, key=itemgetter(3), reverse=True)
    v7 = v3[0][3]
    v8 = v3[0][0]
    v3 = sorted(v3, key=itemgetter(2), reverse=True)
    if v7 * v8 >= v2 - v6:
        v9 = math.ceil((v2 - v6) / v7)
        for v10 in range(len(v3)):
            if v3[v10][3] * v3[v10][0] + v3[v10][1] >= v2 - v6:
                v9 = min(v9, v3[v10][0])
        v5 += v9
        break
    else:
        v5 += v3[0][0]
        v6 += v3[0][3] * v3[0][0] + v3[0][1]
        v3.pop(0)
print(v5)
