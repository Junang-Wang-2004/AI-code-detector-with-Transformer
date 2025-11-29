v1 = list(map(int, input().split()))
v1.sort()
v2 = 0
for v3 in range(0, len(v1) - 2):
    for v4 in range(v3 + 1, len(v1) - 1):
        for v5 in range(v4 + 1, len(v1)):
            if v1[v3] + v1[v4] > v1[v5] and v1[v4] + v1[v5] > v1[v3] and (v1[v5] + v1[v3] > v1[v4]):
                v2 += 1
print(v2)
