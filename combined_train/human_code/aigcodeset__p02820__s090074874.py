v1, v2 = map(int, input().split())
v3, v4, v5 = map(int, input().split())
v6 = input()
v7 = {'s': v3, 'p': v4, 'r': v5}
v8 = 0
for v9 in range(v2):
    v10 = []
    for v11 in range(v1):
        if v9 + v11 * v2 > v1 - 1:
            break
        else:
            v10.append(v6[v9 + v11 * v2])
    v12 = True
    v13 = v10[0]
    v8 += v7[v13]
    for v11 in range(1, len(v10)):
        if v13 == v10[v11] and v12:
            v12 = False
        else:
            v8 += v7[v10[v11]]
            v12 = True
        v13 = v10[v11]
print(v8)
