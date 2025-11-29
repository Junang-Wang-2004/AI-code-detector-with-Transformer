v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v1):
    v5 = int(input())
    v3.append(v5)
v3.sort()
v6 = v3[v1 - 1]
for v7 in range(v1 - v2 + 1):
    v6 = min(v6, v3[v7 + v2 - 1] - v3[v7])
print(v6)
