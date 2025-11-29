import sys
input = sys.stdin.readline
from collections import deque
v1 = 10 ** 9 + 7
v2, v3 = [int(x) for v4 in input().split()]
v5 = [[] for v6 in range(v2)]
for v6 in range(v2 - 1):
    v7, v8 = [int(v4) for v4 in input().split()]
    v5[v7 - 1].append(v8 - 1)
    v5[v8 - 1].append(v7 - 1)
v9 = [-1] * v2
v10 = v3

def f1(a1):
    global ans
    v1 = deque([a1])
    v9[a1] = v3
    while v1:
        v2 = v1.popleft()
        v3 = 0
        if v2 == 0:
            v4 = v3 - 1
        else:
            v4 = v3 - 2
        for v5 in v5[v2]:
            if v9[v5] < 0:
                v9[v5] = v4 - v3
                v3 += 1
                v6 *= v9[v5]
                v6 %= v1
                v1.append(v5)
f1(0)
print(v10)
