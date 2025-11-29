v1, v2, v3 = map(int, input().split())
v4 = list(map(int, input().split()))
v5 = 0
for v6 in range(v1 - 1):
    if v4[v6 + 1] - v4[v6] > v3:
        v5 += v3
    else:
        v5 += v2 * (v4[v6 + 1] - v4[v6])
print(v5)
