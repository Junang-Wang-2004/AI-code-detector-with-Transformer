v1, v2 = [int(x) for v3 in input().split()]
v4 = [0 for v3 in range(v2)]
for v5 in range(v1):
    v6 = [int(v3) for v3 in input().split()]
    v7 = v6[0]
    for v8 in range(v7):
        v4[v6[1 + v8] - 1] += 1
print(v4.count(v1))
