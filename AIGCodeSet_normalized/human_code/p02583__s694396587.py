v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4 in range(v1):
    for v5 in range(v4 + 1, v1):
        for v6 in range(v5 + 1, v1):
            if v2[v4] == v2[v6] or v2[v6] == v2[v5] or v2[v4] == v2[v5]:
                continue
            if v2[v4] + v2[v5] > v2[v6] and v2[v4] + v2[v6] > v2[v5] and (v2[v6] + v2[v5] > v2[v4]):
                v3 += 1
print(v3)
