v1, v2 = [int(i) for v3 in input().rstrip().split(' ')]
v4, v5, v6 = [int(v3) for v3 in input().rstrip().split(' ')]
v7 = 0
v8 = input()
v9 = ['p', 'r', 's']
v10 = {'p': v6, 'r': v4, 's': v5}
v11 = []
for v3, v12 in enumerate(v8):
    v13 = v9[v9.index(v12) - 1]
    if v11[v3 - v2] != v13 if v3 >= v2 else True:
        v11 += [v13]
        v7 += v10[v13]
    else:
        v11 += ['#']
print(v7)
