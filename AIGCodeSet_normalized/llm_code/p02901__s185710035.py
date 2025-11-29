v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v2):
    v5 = list(map(int, input().split()))
    v6 = list(map(int, input().split()))
    v3.append([v5, v6])
v7 = []
from collections import defaultdict
v8 = defaultdict(int)
for v9 in range(1, v1 + 1):
    v10 = 10 ** 5
    for v4 in range(len(v3)):
        if v9 in v3[v4][1]:
            v7.append(v9)
            if v9 in v7 and v7.count(v9) == 1:
                v10 = min(v10, int(v3[v4][0][0]))
                v8[v9] = v10
sum = 0
for v11 in v8.values():
    sum += v11
print(sum)
