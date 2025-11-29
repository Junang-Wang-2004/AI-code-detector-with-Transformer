import sys
input = sys.stdin.readline
from bisect import bisect_left

def f1(a1, a2, a3):
    v1 = 0
    for v2 in range(a2):
        v1 += a2 - bisect_left(a1, a3 - a1[v2])
    return v1

def f2(a1, a2, a3, a4, a5):
    while a5 - a4 > 1:
        v1 = (a4 + a5) // 2
        if f1(a1, a2, v1) >= a3:
            a4 = v1
        else:
            a5 = v1
    return a4
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v3.sort()
v4 = [0] * (v1 + 1)
for v5 in range(v1):
    v4[v5 + 1] = v4[v5] + v3[v5]
v6 = f2(v3, v1, v2, v3[0] * 2, v3[v1 - 1] * 2)
v7 = 0
for v5 in range(v1):
    v8 = bisect_left(v3, v6 - v3[v5])
    v7 += v4[v1] - v4[v8] + v3[v5] * (v1 - v8)
v7 -= (f1(v3, v1, v6) - v2) * v6
print(v7)
