import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
v1 = float('inf')
v2 = 10 ** 9 + 7
v3 = v1
v4 = 0
v5 = 0
v6 = 1

def f1(a1):
    v1 = len(a1)
    v2 = [0] * v1
    v3 = 0
    v4 = 0
    for v5 in range(w):
        v6 = 0
        v6 = [0] * v1
        for v7 in range(h):
            v6[bisect.bisect_left(a1, v7)] += S[v7][v5]
        v8 = 0
        for v7 in range(v1):
            if v6[v7] > K:
                return -1
            if v2[v7] + v6[v7] > K:
                v8 = 1
            else:
                v2[v7] += v6[v7]
        if v8:
            v4 |= 1 << v5 - 1
            for v7 in range(v1):
                v2[v7] = v6[v7]
    return v4
    return v4
v7, v8, v9 = map(int, input().split())
v10 = [list(map(int, input())) for v11 in range(v7)]
for v12 in range((v7 - 1) ** 2):
    v13 = []
    for v14 in range(v7 - 1):
        if v12 >> v14 & 1:
            v13.append(v14)
    v13.append(v7)
    v15 = f1(v13)
    if v15 == -1:
        continue
    v3 = min(v3, collections.Counter(bin(v12))['1'] + collections.Counter(bin(v15))['1'])
print(v3)
