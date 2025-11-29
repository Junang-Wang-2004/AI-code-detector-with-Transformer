v1, v2 = map(int, input().split())
v3 = [0] * (v2 + 1)
for v4 in range(v1):
    v5, *v6 = map(int, input().split())
    for v7 in v6:
        v3[v7] += 1
v8 = 0
for v7 in v3:
    if v7 == v1:
        v8 += 1
print(v8)
