v1 = list(map(int, input().split()))
v2 = [list(map(int, input().split())) for v3 in range(v1[0])]
v4 = [0] * (v1[1] + 1)
for v3 in range(v1[0]):
    for v5 in range(v2[v3][0]):
        v6 = v2[v3][v5 + 1]
        v4[v6] += 1
v7 = 0
for v8 in range(len(v4)):
    if v4[v8] == v1[0]:
        v7 += 1
print(v7)
