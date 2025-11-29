v1, v2, v3 = map(int, input().split())
v4 = list(map(int, input().split()))
v5 = [list(map(int, input().split())) for v6 in range(v1)]
v7 = 0
v8 = 0
for v9 in v5:
    for v10 in range(v2):
        v8 += v9[v10] * v4[v10]
    if v8 + v3 > 0:
        v7 += 1
    v8 = 0
print(v7)
