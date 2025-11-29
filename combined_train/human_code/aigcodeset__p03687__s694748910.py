v1 = input()
v2 = len(v1)
v3 = set()
v4 = v1
v5 = ''
v6 = 0
v7 = float('INF')
for v8 in range(v2):
    if v1[v8] not in v3:
        v5 = v1[v8]
        v3.add(v5)
        while len(set(v4)) != 1:
            v9 = v4
            v4 = ''
            for v10 in range(len(v9) - 1):
                if v9[v10] == v5 or v9[v10 + 1] == v5:
                    v4 += v5
                else:
                    v4 += v1[v10]
            v6 += 1
        if v7 > v6:
            v7 = v6
        v6 = 0
        v4 = v1
print(v7)
