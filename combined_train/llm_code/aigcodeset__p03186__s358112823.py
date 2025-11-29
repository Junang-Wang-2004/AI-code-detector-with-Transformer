v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v2):
    v5 = int(input())
    v3.append(v5)
import math
if v2 == 0:
    v6 = 0
elif v3[math.ceil(v2 / 2) - 1] < v1 / 2:
    v6 = v3[v2 - 1]
    v4 = 0
    v7 = v2 - 1
    while v4 <= math.floor(v2 / 2) - 1 and v7 >= math.ceil(v2 / 2) - 1:
        v6 += abs(v3[v7] - v3[v4])
        v7 -= 1
        v4 += 1
else:
    v6 = 0
    v4 = 0
    v7 = v2 - 1
    while v4 <= math.floor(v2 / 2) - 1 and v7 >= math.ceil(v2 / 2) - 1:
        v6 += abs(v3[v4] - v3[v7])
        v7 -= 1
        v4 += 1
print(v6)
