from math import factorial

def f1(a1, a2):
    return factorial(a1) // factorial(a2) // factorial(a1 - a2)
v1, v2, v3 = map(int, input().split())
v4 = list(map(int, input().split()))
v4.sort()
v5 = v4[-1]
v6 = 0
for v7 in range(1, v2 + 1):
    v6 += v4[-v7]
    v5 = v4[-v7]
v6 = v6 / v2
print(v6)
v8 = 0
import bisect
v9 = v1 - bisect.bisect_right(v4, v5)
if v5 == v4[-1]:
    v10 = v4.count(v5)
    for v7 in range(v2, min(v3, v4.count(v5)) + 1):
        v11 = v7 - v9
        v8 += f1(v10, v11)
else:
    v11 = v2 - v9
    v10 = v4.count(v5)
    v8 += f1(v10, v11)
print(int(v8))
