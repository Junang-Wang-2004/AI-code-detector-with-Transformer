import queue
v1, v2 = map(int, input().split())
v3 = [input() for v4 in range(v1)]
v5 = queue.Queue()
v6 = [-1] * (v1 * v2)
v7 = [0, 1, 0, -1]
v8 = [1, 0, -1, 0]

def f1(a1, a2):
    v1 = a1 // v2
    v2 = a1 % v2
    for v3 in range(4):
        v4 = v1 + v8[v3]
        v5 = v2 + v7[v3]
        if v4 >= 0 and v4 < v1 and (v5 >= 0) and (v5 < v2):
            v6 = v4 * v2 + v5
            if v6[v6] != -1:
                continue
            if a2 == '#':
                if v3[v4][v5] == '.':
                    v6[v6] = v6[a1]
                    f1(v6, '.')
            elif v3[v4][v5] == '#':
                v6[v6] = v6[a1]
                f1(v6, '#')
for v4 in range(v1 * v2):
    v9 = v4 // v2
    v10 = v4 % v2
    if v3[v9][v10] == '#':
        if v6[v4] != -1:
            continue
        v6[v4] = v4
        f1(v4, '#')
v11 = 0
v12 = [0] * (v1 * v2 + 1)
for v4 in range(v1):
    for v13 in range(v2):
        if v3[v4][v13] == '.':
            v12[v6[v4 * v2 + v13]] += 1
for v4 in range(v1):
    for v13 in range(v2):
        if v3[v4][v13] == '#':
            v11 += v12[v6[v4 * v2 + v13]]
print(v11)
