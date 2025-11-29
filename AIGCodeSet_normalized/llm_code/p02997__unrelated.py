v1 = int(input())
v2 = int(input())
if v2 > v1 * (v1 - 1) // 2:
    print(-1)
else:
    v3 = v1 * (v1 - 1) // 2 - v2
    print(v3)
    for v4 in range(1, v1 + 1):
        for v5 in range(v4 + 1, v1 + 1):
            if (v4, v5) not in edges and (v5, v4) not in edges:
                edges.add((v4, v5))
                print(v4, v5)
    for v4 in range(1, v3 + 1):
        for v5 in range(v4 + 1, v3 + 1):
            if (v4, v5) not in edges and (v5, v4) not in edges:
                edges.add((v4, v5))
                print(v4, v5)
