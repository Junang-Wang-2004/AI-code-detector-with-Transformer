v1, v2 = map(int, input().split())
v3 = v1 - 2
for v4 in range(3, v1):
    v3 += v1 - v4
if v3 < v2:
    print(-1)
else:
    v5 = []
    v5.append([1, 2])
    for v4 in range(3, v1 + 1):
        v5.append([2, v4])
    v6 = v3 - v2
    for v4 in range(3, v1 + 1):
        if v6 > 0:
            v5.append([1, v4])
            v6 -= 1
        else:
            break
    for v4 in range(3, v1):
        if not v6 > 0:
            break
        for v7 in range(v4 + 1, v1 + 1):
            if not v6 > 0:
                break
            v5.append([v4, v7])
            v6 -= 1
    v8 = len(v5)
    print(v8)
    for v9 in v5:
        print(*v9)
