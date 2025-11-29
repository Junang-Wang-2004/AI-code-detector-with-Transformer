v1 = int(input())
v2 = []
for v3 in range(v1):
    v4 = int(input())
    v2.append(v4)
v2.sort()
v5 = ['' for v3 in range(v1)]
v5[v1 // 2] = v2[-1]
v2.remove(v2[-1])
v6 = v1 // 2 - 1
v7 = v1 // 2 + 1
for v3 in range(v1 - 1):
    if v3 % 4 == 0:
        v5[v6] = v2[0]
        v2.remove(v2[0])
        v6 -= 1
    elif v3 % 4 == 1:
        v5[v7] = v2[0]
        v2.remove(v2[0])
        v7 += 1
    elif v3 % 4 == 2:
        v5[v6] = v2[-1]
        v2.remove(v2[-1])
        v6 -= 1
    elif v3 % 4 == 3:
        v5[v7] = v2[-1]
        v2.remove(v2[-1])
        v7 -= 1
v5.append(v5[0])
v8 = 0
v9 = 0
v10 = 0
for v3 in range(v1):
    v8 += abs(v5[v3] - v5[v3 + 1])
v8 -= min(abs(v5[0] - v5[1]), abs(v5[-1] - v5[-2]), abs(v5[-2] - v5[-3]))
print(v8)
