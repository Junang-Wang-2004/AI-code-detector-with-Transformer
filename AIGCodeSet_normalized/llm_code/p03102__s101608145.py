v1, v2, v3 = map(int, input().split())
v4 = [i for v5 in map(int, input().split())]
v6 = []
for v7 in range(v1):
    v6.append([v5 for v5 in map(int, input().split())])
v8 = [0] * v1
v9 = 0
for v5 in range(v1):
    for v7 in range(v2):
        v8[v5] += v6[v5][v7] * v4[v7]
    if v8[v5] + v3 > 0:
        v9 += 1
print(v9)
