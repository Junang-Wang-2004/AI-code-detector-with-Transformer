v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v2):
    v5 = list(map(int, input().split()))
    v3.append(v5)
v6 = []
v6.append(v3[0])
v7 = 1
for v8 in v3[1:]:
    v9 = 0
    for v10 in v6:
        if v10[0] < v8[0] and v8[0] < v10[1]:
            v10[0] = v8[0]
            v9 = 1
        elif v10[1] > v8[1] and v8[1] > v10[0]:
            v10[1] = v8[1]
            v9 = 1
        if v9 == 1:
            break
    if v9 == 0:
        v7 = v7 + 1
        v6.append(v8)
print(v7)
