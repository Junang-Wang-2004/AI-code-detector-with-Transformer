v1 = int(input())
v2 = input()
v2 = v2.split()
v3 = []
v4 = {}
for v5 in v2:
    v5 = int(v5)
    v3.append(int(v5))
    if v5 not in v4:
        v4[v5] = 1
    else:
        v4[v5] += 1
v3 = sorted(v3)
v6 = []
for v7, v8 in v4.items():
    v6.append(v7)
v6 = sorted(v6)
v9 = []
v10 = 0
v11 = len(v6)
for v5 in range(v11 - 2):
    for v12 in range(v5 + 1, v11 - 1):
        for v13 in range(v12 + 1, v11):
            if v6[v5] + v6[v12] <= v6[v13]:
                break
            v10 += v4[v6[v5]] * v4[v6[v12]] * v4[v6[v13]]
print(v10)
