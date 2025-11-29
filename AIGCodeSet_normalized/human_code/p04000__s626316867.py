from collections import Counter
import sys
import itertools
input = sys.stdin.readline
v1 = Counter()
v2, v3, v4 = map(int, input().split())
for v5 in range(v4):
    v6, v7 = map(int, input().split())
    for v8, v9 in itertools.product([-1, 0, 1], repeat=2):
        v10 = v6 + v8
        v11 = v7 + v9
        if 2 <= v10 <= v2 - 1 and 2 <= v11 <= v3 - 1:
            v1[v10, v11] += 1
v12 = Counter(v1.values())
v12[0] = (v2 - 2) * (v3 - 2) - sum(v12.values())
for v13 in range(10):
    print(v12[v13])
