from sys import stdin, stdout
import math
import bisect
import datetime
v1 = int(stdin.readline().strip())
v2 = list(map(int, stdin.readline().strip().split()))
v2.insert(0, 0)
v3 = {}
for v4 in range(len(v2)):
    v3[v4] = v2[v4]
v2 = sorted(v3.items(), key=lambda a: a[1])
v5 = [[0 for v4 in range(2005)] for v6 in range(2005)]
for v4 in range(1, v1 + 1):
    v5[v4][v4] = v2[1][1] * abs(v2[1][0] - v4)
for v7 in range(2, v1 + 1):
    v8, v9 = v2[v7]
    for v10 in range(1, v1 - v7 + 2):
        v11 = v10 + v7 - 1
        v5[v10][v11] = max(v5[v10 + 1][v11] + v9 * abs(v8 - v10), v5[v10][v11 - 1] + v9 * abs(v8 - v11))
stdout.writelines(str(v5[1][v1]) + '\n')
