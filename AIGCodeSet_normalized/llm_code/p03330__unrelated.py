import sys
from typing import List
v1 = sys.stdin.readline
v2, v3 = map(int, v1().split())
v4: List[List[int]] = [list(map(int, v1().split())) for v5 in range(v3)]
v6: List[List[int]] = [list(map(int, v1().split())) for v5 in range(v2)]
v7 = [[0] * v3 for v5 in range(3)]
for v8 in range(v2):
    for v9 in range(v2):
        v10 = (v8 + v9) % 3
        v11 = v6[v8][v9] - 1
        for v12 in range(v3):
            if v12 != v11:
                v7[v10][v12] += v4[v11][v12]
v13 = 0
for v8 in range(v2):
    for v9 in range(v2):
        v10 = (v8 + v9) % 3
        v11 = v6[v8][v9] - 1
        v13 += min(v7[v10][v11], min(v7[0][v11], v7[1][v11], v7[2][v11]))
print(v13)
