from collections import defaultdict
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = [0] * (v1 + 1)
for v5 in range(v1):
    v4[v5 + 1] = v4[v5] + v3[v5]
v6 = 0
v7 = defaultdict(int)
for v8 in range(v1 + 1):
    if v8 - v2 >= 0:
        v7[(v4[v8 - v2] - (v8 - v2)) % v2] -= 1
    v6 += v7[(v4[v8] - v8) % v2]
    v7[(v4[v8] - v8) % v2] += 1
print(v6)
