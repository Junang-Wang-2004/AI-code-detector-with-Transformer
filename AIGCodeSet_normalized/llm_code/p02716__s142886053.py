v1 = int(input())
v2 = [int(x) for v3 in input().split()]
v4 = []
v5 = []
v6 = 0
v7 = 0
for v8 in range(v1):
    if v8 % 2 == 0:
        v6 += v2[v8]
        v4.append(v6)
    else:
        v7 += v2[v8]
        v5.append(v7)
v9 = max(v4[-1], v5[-1])
if v1 % 2 != 0:
    for v8 in range(v1):
        if v8 % 2 == 0:
            v9 = max(v9, v4[-1] - v2[v8])
for v8 in range(len(v5)):
    if v8 >= len(v4) - 2:
        continue
    v9 = max(v9, v5[v8] + v4[-1] - v4[v8 + 1])
for v8 in range(len(v4)):
    if v8 >= len(v5) - 2:
        continue
    v9 = max(v9, v4[v8] + v5[-1] - v5[v8 + 1])
if v1 % 2 != 0 and v1 >= 7:
    v10 = [False] * len(v5)
    for v8 in range(len(v5)):
        v10[v8] = v4[v8] - v5[v8]
    v11 = 0
    v12 = v10[0]
    for v8 in range(len(v5)):
        if v8 >= len(v5) - 2:
            continue
        v9 = max(v9, v5[v8] + v4[-1] - v4[v8 + 1])
        if v12 < v10[v8]:
            v11 = v8
            v12 = v10[v8]
        v9 = max(v9, v5[v8] + v4[-1] - v4[v8 + 1] - v5[v11] + v4[v11])
print(v9)
