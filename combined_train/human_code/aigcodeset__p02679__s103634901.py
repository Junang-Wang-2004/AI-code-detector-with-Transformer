v1 = 10 ** 9 + 7
import sys
from collections import defaultdict
input = sys.stdin.readline
v2 = int(input())
v3 = [list(map(int, input().split())) for v4 in range(v2)]

def f1(a1, a2):
    while a1:
        a2, a1 = (a1, a2 % a1)
    return a2
v5 = 0
v6 = []
for v7, v8 in v3:
    v9 = f1(v7, v8)
    if v9 == 0:
        v6.append((0, 0))
        continue
    v6.append((v7 // v9, v8 // v9))
v10 = defaultdict(int)
v11 = defaultdict(int)
v12 = 0
v13 = 0
v14 = 0
v15 = []
for v7, v8 in v6:
    if v7 == 0 and v8 == 0:
        v14 += 1
        continue
    if v7 == 0:
        v12 += 1
        continue
    if v8 == 0:
        v13 += 1
        continue
    if v8 > 0:
        v10[v7, v8] += 1
        v15.append((v7, v8))
    else:
        v11[-v8, v7] += 1
        v15.append((-v8, v7))
v15 = list(set(v15))
v5 = 1
for v16 in v15:
    v17 = v10[v16]
    v18 = v11[v16]
    v5 *= pow(2, v17, v1) + pow(2, v18, v1) - 1
    v5 %= v1
v5 *= pow(2, v13, v1) + pow(2, v12, v1) - 1
v5 -= 1
v5 += v14
print(v5 % v1)
