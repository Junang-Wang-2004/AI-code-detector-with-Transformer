from itertools import permutations
from collections import defaultdict
v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v2)]
v5 = [list(map(int, input().split())) for v4 in range(v1)]
v6 = [defaultdict(int) for v7 in range(3)]
for v4 in range(v1):
    for v8 in range(v1):
        v6[(v4 + v8 + 2) % 3][v5[v4][v8] - 1] += 1

def f1(a1, a2):
    v1 = 0
    for v2, v3 in a1.items():
        v1 += v3[v2][a2] * v3
    return v1
v9 = 10 ** 9
v10 = v9
for v11 in permutations(range(v2), 3):
    v12 = 0
    for v4 in range(3):
        v12 += f1(v6[v4], v11[v4])
    v10 = min(v10, v12)
print(v10)
