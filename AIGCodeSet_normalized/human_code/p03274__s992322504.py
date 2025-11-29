v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = [0] * v1
for v5 in range(v1 - 1):
    v4[v5 + 1] = abs(v3[v5 + 1] - v3[v5]) + v4[v5]
v6 = [0] * v1
for v5 in range(1, v1)[::-1]:
    v6[v5 - 1] = abs(v3[v5] - v3[v5 - 1]) + v6[v5]
v7 = float('inf')
for v5 in range(v1 - v2 + 1):
    v7 = min(v7, abs(v3[v5]) + v4[v5 + v2 - 1] - v4[v5])
for v5 in range(v2 - 1, v1)[::-1]:
    v7 = min(v7, abs(v3[v5]) + v6[v5 - v2 + 1] - v6[v5])
print(v7)
