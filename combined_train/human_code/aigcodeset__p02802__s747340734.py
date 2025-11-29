v1, v2 = [int(i) for v3 in input().split()]
v4 = []
for v3 in range(v2):
    v5 = input().split()
    v6 = int(v5[0]) - 1
    v7 = str(v5[1])
    v4.append([v6, v7])
v8 = [0 for v3 in range(v1)]
v9 = [0 for v3 in range(v1)]
v10 = [0 for v3 in range(v1)]
for v6, v7 in v4:
    if v8[v6] == 0 and v7 == 'AC':
        v8[v6] = 1
    elif v8[v6] == 0 and v7 == 'WA':
        v9[v6] += 1
v11 = 0
for v6 in range(v1):
    if v8[v6] == 1:
        v11 += v9[v6]
print(sum(v8), v11)
