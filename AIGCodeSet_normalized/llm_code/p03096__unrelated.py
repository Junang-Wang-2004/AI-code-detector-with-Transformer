import sys
from collections import defaultdict
v1 = 10 ** 9 + 7
v2 = int(sys.stdin.readline())
v3 = [int(sys.stdin.readline()) for v4 in range(v2)]
v5 = defaultdict(list)
for v6, v7 in enumerate(v3):
    v5[v7].append(v6)
v8 = [0] * (v2 + 1)
v8[0] = 1
for v7, v9 in v5.items():
    for v6 in range(len(v9) - 1, -1, -1):
        for v10 in range(v6 - 1, -1, -1):
            v8[v9[v6] + 1] = (v8[v9[v6] + 1] + v8[v9[v10] + 1]) % v1
print(v8[v2])
