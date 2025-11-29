v1 = int(input())
v2 = [list(map(int, input().split())) for v3 in range(v1)]
v4 = 0
for v5 in range(v1):
    for v3 in range(v1):
        for v6 in range(v1):
            if v2[v3][v6] > v2[v3][v5] + v2[v5][v6]:
                print(-1)
                exit()
for v3 in range(v1 - 1):
    for v6 in range(v3 + 1, v1):
        for v5 in range(v1):
            if v5 == v3 or v5 == v6:
                continue
            if v2[v3][v6] == v2[v3][v5] + v2[v5][v6]:
                break
        else:
            v4 += v2[v3][v6]
print(v4)
