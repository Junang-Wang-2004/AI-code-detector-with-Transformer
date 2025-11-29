v1 = int(input())
v2 = [[[], 0]]
for v3 in range(v1):
    v4 = []
    for v5, v6 in v2:
        for v7 in range(v6 + 1):
            v8 = v5[:]
            v8.append(v7)
            if v7 == v6:
                v4.append([v8, v6 + 1])
            else:
                v4.append([v8, v6])
    v2 = v4
v9 = []
v10 = ord('a')
for v5, v11 in v2:
    v9.append(''.join(map(lambda x: chr(x + v10), v5)))
v9.sort()
print(*v9, sep='\n')
