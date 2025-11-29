v1, v2 = map(int, input().split())
v3 = [0 for v4 in range(v2)]
for v5 in range(v1):
    v6, *v7 = list(map(int, input().split()))
    for v8 in range(v6):
        v3[v7[v8] - 1] += 1
v9 = 0
for v5 in range(v2):
    if v3[v5] == v1:
        v9 += 1
print(v9)
