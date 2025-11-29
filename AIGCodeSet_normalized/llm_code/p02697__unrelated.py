v1, v2 = map(int, input().split())
v3 = []
for v4 in range(1, v2 + 1):
    v3.append((v4, v4 + v2))
for v4 in range(v2 + 1, v1 + 1):
    for v5 in range(v2):
        if v4 not in v3[v5]:
            v3[v5] = (v3[v5][0], v4) if v3[v5][0] != 0 else (v4, v3[v5][1])
            break
for v6 in v3:
    print(*v6)
