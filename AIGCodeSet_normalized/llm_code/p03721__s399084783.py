from collections import defaultdict
v1, v2 = map(int, input().split())
v3 = 0
sum = 0
v4 = defaultdict(int)
for v5 in range(v1):
    v6, v7 = map(int, input().split())
    v4[v6] += v7
v8 = sorted(v4.items())
for v9, v10 in v8:
    sum += v10
    if sum >= v2:
        print(v9)
        exit()
