v1 = int(input())
v2 = list(input())
v3 = 0
for v4 in range(v1 - 2):
    for v5 in range(v4 + 1, v1 - 1):
        if v2[v4] == v2[v5]:
            continue
        for v6 in range(v5 + 1, v1):
            if v2[v4] != v2[v6] and v2[v5] != v2[v6] and (v5 - v4 != v6 - v5):
                v3 += 1
print(v3)
