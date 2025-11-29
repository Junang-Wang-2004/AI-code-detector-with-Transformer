import math
from collections import deque
v1 = deque([1, 2])
v2 = 1

def f1(a1):
    global memo, floor
    while a1 > v2:
        v1.append(v1[-1] + v1[-2])
        v1 += 1
    return v1[a1 - 1]
v3 = 1000000007
v4, v5 = map(int, input().split())
v6 = []
v7 = -1
for v8 in range(v5):
    v9 = int(input())
    if v7 + 1 == v9:
        print(0)
        exit()
    v6.append(v9 - v7 - 2)
    v7 = v9
v6.append(v4 - v7 - 1)
v10 = 1
for v11 in v6:
    if v11 == 0:
        continue
    v10 = v10 * f1(v11) % v3
print(v10)
