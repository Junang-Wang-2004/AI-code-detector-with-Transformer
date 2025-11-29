import math
v1, v2 = map(int, input().split(' '))
v3 = list(map(int, input().split(' ')))
v4 = sum(v3)
v5 = []
v6 = 1
v7 = 1
while v6 * v6 <= v4:
    if v4 % v6 == 0:
        v5.append(v6)
        v5.append(v4 // v6)
    v6 += 1
v5.sort(reverse=True)
for v6 in v5:
    v8 = 0
    v9 = []
    for v10 in v3:
        v9.append(v10 % v6)
        v8 += v10 % v6
    if v8 % v6 != 0:
        continue
    else:
        v11 = 0
        v9.sort()
        v12 = v8 // v6
        for v13 in range(0, v1 - v12):
            v11 += v9[v13]
        if v11 <= v2:
            v7 = v6
            break
print(v7)
