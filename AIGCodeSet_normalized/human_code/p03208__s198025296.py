v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v1):
    v3.append(int(input()))
v5 = float('inf')
v3.sort()
v6 = v5
for v7 in range(v2 - 1, v1):
    v6 = min(v6, v3[v7] - v3[v7 - v2 + 1])
print(v6)
