import math
v1 = int(input())
v2 = [list(map(int, input().split())) for v3 in range(v1)]
v4 = 1
v5 = 1
v6 = 2
for v7 in range(0, v1):
    v8 = max(-(-v4 // v2[v7][0]), -(-v5 // v2[v7][1]))
    v4 = v2[v7][0] * v8
    v5 = v2[v7][1] * v8
    v6 = v4 + v5
print(v6)
