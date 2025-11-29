v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = 0
from collections import Counter
v5 = Counter()
v5[0] = 1
v6 = 0
v7 = [0] * (v1 + 1)
for v8, v9 in enumerate(v3):
    if v8 >= v2 - 1:
        v5[v7[v8 - (v2 - 1)]] -= 1
    v4 = (v4 + v9 - 1) % v2
    v6 += v5[v4]
    v5[v4] += 1
    v7[v8 + 1] = v4
print(v6)
