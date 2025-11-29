v1, v2 = map(int, input().split())
v3 = []
v4 = []
for v5 in range(v1):
    v3.append(list(map(int, input().split())))
for v5 in range(v2):
    v4.append(list(map(int, input().split())))
v6 = []
for v5 in range(v1):
    v7 = []
    for v8 in range(v2):
        v9 = abs(v3[v5][0] - v4[v8][0]) + abs(v3[v5][1] - v4[v8][1])
        v7.append(v9)
    v10 = v7.index(min(v7))
    v6.append(v10)
for v5 in range(len(v6)):
    print(v6[v5] + 1)
