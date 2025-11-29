import math
v1 = int(input())
v2 = [0] * v1
v3 = [0] * v1
for v4 in range(v1):
    v5, v6 = map(int, input().split())
    if v4 == 0:
        v2[0] = v5
        v3[0] = v6
    else:
        v7 = math.ceil(max(v2[v4 - 1] / v5, v3[v4 - 1] / v6))
        v2[v4] = v7 * v5
        v3[v4] = v7 * v6
print(int(v2[-1] + v3[-1]))
