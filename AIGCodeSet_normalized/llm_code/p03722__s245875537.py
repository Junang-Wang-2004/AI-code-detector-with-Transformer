v1, v2 = map(int, input().split())
v3 = []
v4 = ['None' for v5 in range(v1)]
v4[0] = 0
for v5 in range(v2):
    v6, v7, v8 = map(int, input().split())
    v3.append([v6 - 1, v7 - 1, v8])
for v5 in range(2 * v1):
    for v9 in v3:
        if v4[v9[1]] == 'None' and v4[v9[0]] != 'None':
            v4[v9[1]] = v4[v9[0]] + v9[2]
        if v4[v9[1]] != 'None' and v4[v9[0]] != 'None':
            if v4[v9[1]] < v4[v9[0]] + v9[2]:
                v4[v9[1]] = v4[v9[0]] + v9[2]
    if v5 == v1 - 1:
        v10 = v4[v1 - 1]
    if v5 == 2 * v1 - 1:
        if v10 != v4[v1 - 1]:
            v4[v1 - 1] = 1000000000000000.0
if v4[v1 - 1] < 1000000000000000.0:
    print(v10)
else:
    print('inf')
