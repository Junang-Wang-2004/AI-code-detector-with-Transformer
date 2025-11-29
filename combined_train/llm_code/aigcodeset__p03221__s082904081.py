v1, v2 = map(int, input().split())
v3, v4 = ([], [])
for v5 in range(v2):
    v6, v7 = map(int, input().split())
    v3.append(v6)
    v4.append(v7)
v8 = sorted(zip(v3, v4, range(v2)))
v3, v4, v9 = zip(*v8)
v10 = []
v11 = v3[0]
v12 = 1
for v5 in range(v2):
    if v11 == v3[v5]:
        v10.append(f'{v3[v5]:06d}{v12:06d}')
        v12 += 1
    else:
        v12 = 1
        v11 = v3[v5]
        v10.append(f'{v3[v5]:06d}{v12:06d}')
v13 = sorted(zip(v9, v10))
v9, v10 = zip(*v13)
for v5 in v10:
    print(v5)
