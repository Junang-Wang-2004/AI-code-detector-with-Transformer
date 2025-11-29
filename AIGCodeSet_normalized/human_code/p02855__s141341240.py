v1, v2, v3 = map(int, input().split())
v4 = [list(input()) for v5 in range(v1)]
v6 = 1
v7 = []
for v8 in range(v1):
    if '#' not in v4[v8]:
        v7.append(v8)
        if v8 == v1 - 1:
            for v8 in range(len(v7)):
                print(*ans)
        continue
    v9 = 0
    v10 = 0
    v11 = []
    while v9 < v2:
        if v4[v8][v9] == '#':
            for v12 in range(v9 - v10 + 1):
                v11.append(v6)
            if v9 < v2 - 1 and '#' not in v4[v8][v9 + 1:]:
                for v13 in range(v2 - v9 - 1):
                    v11.append(v6)
            v10 = v9 + 1
            v6 += 1
        v9 += 1
    v14 = v11
    print(*v11)
    while v7:
        print(*v11)
        v7.pop()
