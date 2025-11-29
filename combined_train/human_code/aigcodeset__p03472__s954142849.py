import math
v1, v2 = map(int, input().split())
v3, v4 = ([], [])
for v5 in range(v1):
    v6, v7 = map(int, input().split())
    v3.append(v6)
    v4.append(v7)
v8 = max(v3)
v9 = [x for v10 in v4 if v8 < v10]
if sum(v9) >= v2:
    v11 = 0
    v12 = 0
    for v13 in sorted(v9)[::-1]:
        v11 += v13
        v12 += 1
        if v11 >= v2:
            print(v12)
            exit()
v2 -= sum(v9)
v14 = len(v9) + math.ceil(v2 / v8)
print(v14)
