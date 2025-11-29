def f1():
    return list(map(int, input().split()))
v1, v2 = f1()
v3 = f1()
v4 = sum(v3)
v5 = int(v4 ** 0.5 // 1) + 1
v6 = []
for v7 in range(1, v5):
    if v4 % v7 == 0:
        v6.append(v7)
v8 = len(v6)
for v7 in range(v8):
    v6.append(v4 // v6[v7])
v6 = sorted(v6)
v9 = 1
for v7 in v6:
    v10 = []
    for v11 in v3:
        v8 = v11 % v7
        if v8 != 0:
            v10.append([v8, v7 - v8])
    v10 = sorted(v10)
    v12 = 0
    v13 = 0
    for v11 in range(len(v10)):
        v12 += v10[v11][0]
    v14 = 0
    for v11 in range(len(v10)):
        v12 -= v10[-1 - v11][0]
        v13 += v10[-1 - v11][1]
        v14 += v10[-1 - v11][1]
        if v12 == v13:
            break
    if v14 <= v2:
        v9 = v7
print(v9)
