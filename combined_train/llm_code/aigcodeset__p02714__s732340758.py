v1 = int(input())
v2 = input()
v3 = []
v4 = []
v5 = []
v6 = 0
v7 = 0
v8 = 0
for v9 in range(v1):
    if v2[v9] == 'R':
        v3.append(v9)
        v6 += 1
    elif v2[v9] == 'G':
        v4.append(v9)
        v7 += 1
    else:
        v5.append(v9)
        v8 += 1
v10 = 0
for v9 in range(v1 - 2):
    for v11 in range(v9 + 1, v1 - 1):
        v12 = 2 * v11 - v9
        if v12 < v1:
            if v2[v9] != v2[v11] and v2[v9] != v2[v12] and (v2[v12] != v2[v11]):
                v10 += 1
                print(v9, v11, v12)
print(v10)
print(v6 * v7 * v8 - v10)
