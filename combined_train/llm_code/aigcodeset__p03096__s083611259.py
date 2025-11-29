import sys
input = sys.stdin.readline
v1 = int(input())
v2 = []
v3 = 0
v4 = 0
for v5 in range(v1):
    v6 = int(input())
    if v6 != v3:
        v2.append(v6)
        v3 = v6
        v4 += 1
v1 = v4
from collections import Counter
v7 = Counter()
v8 = 1
v9 = 10 ** 9 + 7
for v5 in range(v1):
    if v5 == 0 or v5 == v1 - 1:
        v7[v2[v5]] += 1
    elif v2[v5] == v2[v5 - 1]:
        v7[v2[v5]] += v7[v2[v5 - 1]]
    else:
        v7[v2[v5]] += 1
    v8 = v8 * v7[v2[v5]] % v9
print(v8)
