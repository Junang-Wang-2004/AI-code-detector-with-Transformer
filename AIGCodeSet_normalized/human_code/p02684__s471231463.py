from collections import defaultdict
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = defaultdict(list)
v5 = 1
v6 = []
for v7 in range(v2):
    v4[v5].append(v7)
    v6.append(v5)
    if len(v4[v5]) == 2:
        v8 = v4[v5][0]
        v9 = v7
        v10 = (v2 - v8) % (v9 - v8)
        v5 = v6[v8 + v10]
        break
    v5 = v3[v5 - 1]
print(v5)
