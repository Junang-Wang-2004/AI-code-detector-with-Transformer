v1 = int(input())
v2 = list(map(int, input().split()))
from collections import defaultdict
v3 = defaultdict(int)
for v4 in v2:
    v3[v4] += 1
v5 = 0
for v6 in set(v2):
    v7 = v3[v6]
    if v6 > v7:
        v5 += v7
    else:
        v5 += v7 - v6
print(v5)
