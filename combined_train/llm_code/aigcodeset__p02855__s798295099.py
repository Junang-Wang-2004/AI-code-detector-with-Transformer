from collections import deque
v1, v2, v3 = map(int, input().split())
v4 = []
v5 = []
for v6 in range(v1):
    v7 = input()
    v7 += '.'
    v4.append(v7)
    for v8 in range(v2):
        if v7[v8] == '#':
            v5.append((v6, v8))
v9 = [[-1] * v2 for v10 in range(v1)]
v11 = 1
for v12 in v5:
    v9[v12[0]][v12[1]] = v11
    v11 += 1
for v12 in v5:
    v13 = deque()
    v13.append(v12)
    v14 = v9[v12[0]][v12[1]]
    while v13:
        v15, v16 = v13.popleft()
        for v6 in range(v16 + 1, v2):
            if v9[v15][v6] < 0:
                v9[v15][v6] = v14
            else:
                v6 -= 1
                break
        for v8 in range(v16 - 1, -1, -1):
            if v9[v15][v8] < 0:
                v9[v15][v8] = v14
            else:
                v8 += 1
                break
        for v17 in range(v15 + 1, v1):
            v18 = True
            for v19 in range(v8, v6 + 1):
                if v9[v17][v19] >= 0:
                    v18 = False
                    break
            if v18:
                for v19 in range(v8, v6 + 1):
                    v9[v17][v19] = v14
            else:
                v17 -= 1
                break
        for v17 in range(v15 - 1, -1, -1):
            v18 = True
            for v19 in range(v8, v6 + 1):
                if v9[v17][v19] >= 0:
                    v18 = False
                    break
            if v18:
                for v19 in range(v8, v6 + 1):
                    v9[v17][v19] = v14
            else:
                v17 += 1
                break
for v6 in range(v1):
    print(*v9[v6])
