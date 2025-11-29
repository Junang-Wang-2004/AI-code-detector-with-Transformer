import sys
import numpy as np
input = sys.stdin.readline

def f1():
    v1 = int(input())
    v2 = np.array(list(map(int, input().split())))
    v3 = v1 // 2
    v4 = v1 // 2
    v5 = {}
    v6 = {}
    for v7 in range(0, v1, 2):
        if v2[v7] in v5:
            v5[v2[v7]] += 1
        else:
            v5[v2[v7]] = 1
    for v7 in range(1, v1, 2):
        if v2[v7] in v6:
            v6[v2[v7]] += 1
        else:
            v6[v2[v7]] = 1
    v8 = sorted(v5.items(), key=lambda x: (-x[1], x[0]))
    v9 = sorted(v6.items(), key=lambda x: (-x[1], x[0]))
    v10, v11 = v8[0]
    v12, v13 = v8[1] if len(v8) > 1 else (0, 0)
    v14, v15 = v9[0]
    v16, v17 = v9[1] if len(v9) > 1 else (0, 0)
    if v10 != v14:
        print(v1 - v11 - v15)
    else:
        print(min(v1 - v11 - v17, v1 - v13 - v15))
if __name__ == '__main__':
    f1()
