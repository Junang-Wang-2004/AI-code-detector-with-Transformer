v1, v2 = [int(_) for v3 in input().split()]
v4 = {}
for v5 in range(v1):
    v4[v5] = {}
for v3 in range(v2):
    v6, v7, v8 = [int(v3) for v3 in input().split()]
    v6 -= 1
    v7 -= 1
    v4[v6][v7] = -v8
v9 = float('inf')
v10 = [v9] * v1
v10[0] = 0
v11 = 0
while True:
    v11 += 1
    v12 = False
    v13 = False
    for v6 in v4.keys():
        for v7 in v4[v6].keys():
            if v10[v6] != v9 and v10[v7] > v10[v6] + v4[v6][v7]:
                v10[v7] = v10[v6] + v4[v6][v7]
                v12 = True
                if v7 == v1 - 1:
                    v13 = True
    if not v12 or v11 == v1:
        break
if v13:
    print('inf')
else:
    print(-v10[-1])
