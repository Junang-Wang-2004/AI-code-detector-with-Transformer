import math
v1, v2 = map(int, input().split())
v3 = []
v4 = []
v5 = 0
for v6 in range(v1):
    v7, v8 = map(int, input().split())
    v3.append(v7)
    v4.append(v8)
v3.sort()
v4.sort()
for v6 in range(v1 - 1, -1, -1):
    if v3[-1] <= v4[v6]:
        v2 -= v4[v6]
        v5 += 1
        if v2 <= 0:
            break
    else:
        break
v5 += math.ceil(v2 / v3[-1])
print(v5)
