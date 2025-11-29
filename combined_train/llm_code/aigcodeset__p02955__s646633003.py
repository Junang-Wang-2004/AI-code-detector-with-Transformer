import sys
import collections
import copy
import math
input = sys.stdin.readline
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = sum(v3)

def f1(a1):
    v1 = []
    for v2 in range(1, int(a1 ** 0.5) + 1):
        if a1 % v2 == 0:
            v1.append(v2)
            if v2 != a1 // v2:
                v1.append(a1 // v2)
    v1.sort(reverse=True)
    return v1
v5 = f1(v4)
v6 = 0
for v7 in range(len(v5)):
    v8 = v5[v7]
    v9 = 0
    v10 = v8
    v9 += v3[0] % v8
    v11 = [v3[0] % v8]
    for v12 in range(1, v1):
        v9 += v3[v12] % v8
        v11.append(v3[v12] % v8)
    v13 = v9 // v8
    v11.sort(reverse=True)
    v14 = 0
    for v12 in range(v13):
        v14 += v8 - v11[v12]
    if v14 > v2:
        continue
    else:
        print(v8)
        break
