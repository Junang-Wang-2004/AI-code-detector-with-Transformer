from collections import defaultdict
v1, v2 = map(int, input().split())
*v3, = map(int, input().split())
v3 = [0] + v3
v4 = []
v5 = defaultdict(int)
v6 = 0
v7 = 0
for v8, v9 in enumerate(v3):
    v6 += v9 - 1
    v6 %= v2
    v4.append(v6)
    if v8 - v2 >= 0:
        v5[v4[v8 - v2]] -= 1
    v7 += v5[v6]
    v5[v6] += 1
print(v7)
