import math
v1 = int(input())
v2 = [[int(i) for v3 in input().split()] for v3 in range(v1 - 1)]
v4 = []
for v3 in range(v1 - 1):
    v5 = v2[v3][0] + v2[v3][1]
    for v6 in v2[v3 + 1:]:
        if v5 <= v6[1]:
            v5 = v6[0] + v6[1]
            continue
        v5 = math.ceil((v5 - v6[1]) / v6[2]) * v6[2] + v6[1] + v6[0]
    v4.append(v5)
v4.append(0)
for v6 in v4:
    print(v6)
