v1 = int(input())
*v2, = map(int, input().split())
v3, v4 = (max(v2), min(v2))
v5, v6 = (v2.index(v3), v2.index(v4))
v7 = None
if v4 >= 0:
    v7 = 2
elif v3 <= 0:
    v7 = 3
elif v3 >= abs(v4):
    v7 = 0
else:
    v7 = 1
v8 = []
if v7 == 0:
    for v9 in range(v1):
        if v9 != v5:
            v2[v9] += v2[v5]
            v8.append((v5 + 1, v9 + 1))
    v7 += 2
elif v7 == 1:
    for v9 in range(v1):
        if v9 != v6:
            v2[v9] += v2[v6]
            v8.append((v6 + 1, v9 + 1))
    v7 += 2
if v7 == 2:
    for v9 in range(v1 - 1):
        v2[v9 + 1] += v2[v9]
        v8.append((v9 + 1, v9 + 2))
elif v7 == 3:
    for v9 in range(v1 - 1, 0, -1):
        v2[v9 - 1] += v2[v9]
        v8.append((v9 + 1, v9))
print(len(v8))
for v10 in v8:
    print(*v10)
