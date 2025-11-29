v1, v2, v3 = map(int, input().split())
v4 = list(map(int, input().split()))
v5 = 0
v6 = 1
for v7 in range(len(v4) - 1):
    v5 += min((v4[v7 + 1] - v4[v7]) * v2, v3)
print(v5)
