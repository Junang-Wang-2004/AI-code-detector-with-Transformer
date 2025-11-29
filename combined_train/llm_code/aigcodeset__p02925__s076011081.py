def f1():
    import sys
    import time
    input = sys.stdin.buffer.readline
    v1 = time.time()
    v2 = int(input())
    v3 = [tuple(map(int, input().split())) for v4 in range(v2)]
    id = [0] * v2
    v5 = [-1] * v2
    v6 = 0
    v7 = 0
    v8 = v2 * (v2 - 1) // 2
    while v7 < v2 - 1:
        v9 = time.time()
        if v9 - v1 > 2:
            v6 = v8 + 1
            break
        v6 += 1
        if v6 > v8:
            break
        v10 = set()
        for v4 in range(v2):
            if id[v4] >= v2 - 1:
                continue
            elif v5[v4] >= 0:
                continue
            else:
                v11 = v3[v4][id[v4]]
                if v5[v11 - 1] == v4 and id[v11 - 1] < v2 - 1 and (v3[v11 - 1][id[v11 - 1]] == v4 + 1) and (v4 not in v10):
                    v5[v11 - 1] = -1
                    id[v11 - 1] += 1
                    v10.add(v11 - 1)
                    id[v4] += 1
                elif v4 not in v10:
                    v5[v4] = v3[v4][id[v4]] - 1
        v7 = min(id)
    if v6 > v8:
        print(-1)
    else:
        print(v6)
f1()
