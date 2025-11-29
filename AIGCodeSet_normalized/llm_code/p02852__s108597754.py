v1, v2 = map(int, input().split())
v3 = input()
v4 = [-1] * (v1 + 1)
v4[v1] = 0
for v5 in range(v1 - 1, -1, -1):
    if v3[v5] == '1':
        continue
    for v6 in range(1, min(v2, v1 - v5) + 1):
        if v4[v5 + v6] != -1:
            if v4[v5] == -1 or v4[v5] > v4[v5 + v6] + 1:
                v4[v5] = v4[v5 + v6] + 1
if v4[0] == -1:
    print(-1)
else:
    v7 = []
    v5 = 0
    while v5 < v1:
        for v6 in range(min(v2, v1 - v5), 0, -1):
            if v4[v5 + v6] == v4[v5] - 1:
                v7.append(v6)
                v5 += v6
                break
    print(*v7)
