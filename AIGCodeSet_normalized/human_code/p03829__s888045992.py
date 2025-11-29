v1, v2, v3 = map(int, input().split())
v4 = list(map(int, input().split()))
v5 = 0
for v6 in range(v1 - 1):
    v5 += min(v2 * (v4[v6 + 1] - v4[v6]), v3)
print(v5)
