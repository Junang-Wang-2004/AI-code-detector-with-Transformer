v1, *v2 = map(int, open(0).read().split())
v3 = 10 ** 9 + 7
from collections import defaultdict
v4 = {}
v5 = defaultdict(lambda: 1)
for v6, v7 in enumerate(v2):
    v5[v6] = v5[v6 - 1]
    if v7 in v4:
        v8 = v4[v7]
        if v6 - v8 > 1:
            v5[v6] += v5[v8]
            v5[v6] %= v3
    v4[v7] = v6
print(v5[v1 - 1])
