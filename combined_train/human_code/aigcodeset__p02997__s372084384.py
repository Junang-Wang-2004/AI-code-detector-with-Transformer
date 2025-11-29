v1, v2 = map(int, input().split())
if v2 > (v1 - 1) * (v1 - 2) // 2:
    print(-1)
else:
    v3 = 0
    v4 = []
    for v5 in range(2, v1 + 1):
        v3 += 1
        v4.append([1, v5])
    v6 = 0
    v7 = 0
    for v5 in range(2, v1 + 1):
        for v8 in range(v5 + 1, v1 + 1):
            if v6 == (v1 - 1) * (v1 - 2) // 2 - v2:
                v7 = 1
                break
            v3 += 1
            v6 += 1
            v4.append([v5, v8])
        if v7:
            break
    print(v3)
    for v9 in v4:
        print(*v9)
