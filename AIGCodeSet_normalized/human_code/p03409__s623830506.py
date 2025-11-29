v1 = int(input())
v2 = [[int(i) for v3 in input().split()] for v4 in range(v1)]
v5 = [[int(v3) for v3 in input().split()] for v4 in range(v1)]
v2.sort()
v5.sort()
v6 = 0
v7 = []
for v8, v9 in v5:
    for v10, v11 in v2:
        if v8 > v10 and v9 > v11:
            v7.append([v10, v11])
    if v7 != []:
        v12 = max(v7, key=lambda r: r[1])
        v6 += 1
        v2.remove(v12)
        v7 = []
print(v6)
