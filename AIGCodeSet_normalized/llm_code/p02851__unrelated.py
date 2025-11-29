from collections import defaultdict
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = [0] * (v1 + 1)
v5 = defaultdict(int)
v5[0] = 1
v6 = 0
for v7 in range(1, v1 + 1):
    v4[v7] = v4[v7 - 1] + v3[v7 - 1]
    v8 = v4[v7] % v2
    v6 += v5[(v8 - v7) % v2]
    v5[v8] += 1
print(v6)
