v1, v2, v3 = map(int, input().split())
v4 = list(map(int, input().split()))
v5 = [list(map(int, input().split())) for v6 in range(v1)]
v7 = 0
for v8 in range(v1):
    v9 = sum((v5[v8][j] * v4[j] for v10 in range(v2))) + v3
    if v9 > 0:
        v7 += 1
print(v7)
