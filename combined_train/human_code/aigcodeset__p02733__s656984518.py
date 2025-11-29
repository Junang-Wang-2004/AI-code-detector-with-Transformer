from itertools import accumulate
import sys
input = sys.stdin.readline
v1, v2, v3 = map(int, input().split())
v4 = [list(map(int, input().rstrip())) for v5 in range(v1)]
v6 = [list(accumulate(v4[i])) for v7 in range(v1)]
v8 = float('inf')
for v9 in range(1 << v1 - 1):
    v10 = 0
    v11 = -1
    for v12 in range(v1 - 1):
        v10 += v9 >> v12 & 1
    for v13 in range(v2):
        v14 = 0
        v15 = False
        for v12 in range(v1):
            if v12 > 0 and v9 >> v12 - 1 & 1:
                if v14 > v3:
                    v15 = True
                    break
                v14 = 0
            v14 += v6[v12][v13] - (v6[v12][v11] if v11 >= 0 else 0)
        if v14 > v3:
            v15 = True
        if v15:
            if v13 - 1 == v11:
                break
            v10 += 1
            v11 = v13 - 1
            continue
    else:
        v8 = min(v8, v10)
print(v8)
