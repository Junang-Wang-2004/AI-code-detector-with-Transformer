v1 = int(input())
v2 = [list(map(int, input().split())) for v3 in range(v1)]
v4 = []
for v3 in range(v1 - 1):
    for v5 in range(v3 + 1, v1):
        v4.append([v2[v3][0] - v2[v5][0], v2[v3][1] - v2[v5][1]])
v6 = v1
for v3 in v4:
    v7 = []
    for v5 in range(v1):
        v7.append([v2[v5][0] - v3[0], v2[v5][1] - v3[1]])
    v8 = v1
    for v5 in v7:
        if v5 in v2:
            v8 -= 1
    if v8 < v6:
        v6 = v8
print(v6)
