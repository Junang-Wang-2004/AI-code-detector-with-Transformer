import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
v1 = float('inf')
v2 = 10 ** 9 + 7
v3 = v1
v4 = 0
v5 = 0
v6 = 1
v7 = int(input())
v8 = [int(input()) for v9 in range(v7)]
v10 = [-1] * (v7 + 1)
v11 = [-1] * (2 * 10 ** 5 + 1)
for v9, v12 in enumerate(v8):
    if v11[v12] != -1 and abs(v9 - v11[v12]) != 1:
        v10[v11[v12]] = v9
    v11[v12] = v9
v13 = [0] * (v7 + 1)
for v9 in range(v7 - 1, -1, -1):
    if v10[v9] == -1:
        continue
    v14 = v10[v9]
    v4 += v13[v14] + 1
    v4 %= v2
    v13[v9] += 1
    v13[v9 - 1] += v13[v9]
print((v4 + 1) % v2)
