v1, v2, v3 = map(int, input().split())
v4 = list(map(int, input().split()))
v5 = 0
for v6 in range(v1):
    v7 = list(map(int, input().split()))
    v8 = 0
    for v9 in range(v2):
        v8 += v7[v9] * v4[v9]
    if v8 + v3 > 0:
        v5 += 1
print(v5)
