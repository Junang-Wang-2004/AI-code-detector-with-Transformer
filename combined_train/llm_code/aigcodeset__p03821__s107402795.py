import sys
import math
v1 = lambda: int(sys.stdin.readline())
v2 = lambda: map(int, sys.stdin.readline().split())
v3 = lambda: list(v2())
v4 = lambda: map(str, sys.stdin.readline().split())
v5 = lambda: list(v4())
v6 = v1()
v7 = []
v8 = 0
v9 = []
for v10 in range(v6):
    v11, v12 = v2()
    if v12 == 1:
        v9.append(-1)
    elif v12 >= v11:
        v9.append(v12 - v11)
    else:
        v9.append(v12 - v11 % v12)
    v7.append([v11, v12])
for v10 in range(v6)[::-1]:
    if v9[v10] == -1:
        continue
    elif v9[v10] >= v8:
        v8 += v9[v10] - v8
    else:
        v8 += v7[v10][1] - (v7[v10][0] + v8) % v7[v10][1]
print(v8)
