from itertools import *
v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v2)]
v5 = [[0] * v2 for v4 in range(3)]
for v4 in range(v1):
    for v6, v7 in enumerate(map(int, input().split())):
        v5[(v4 + v6) % 3][v7 - 1] += 1
print(min((sum((v5[v6][cmb[v4]] * v3[v4][v6] for v4 in range(v2) for v6 in range(3))) for v8 in permutations(range(v2)))))
