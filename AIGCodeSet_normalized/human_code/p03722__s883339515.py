v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v2):
    v5, v6, v7 = map(int, input().split())
    v3.append((v5, v6, v7))
v8 = [-v1 * 10 ** 9] * (v1 + 1)
v8[1] = 0
v9 = False
for v10 in range(v1):
    for v5, v6, v7 in v3:
        v11 = v8[v5] + v7
        if v11 > v8[v6]:
            v8[v6] = v11
    if v10 == v1 - 1 and v8[v1] > predist:
        v9 = True
    v12 = v8[v1]
if v9:
    print('inf')
else:
    print(v8[v1])
