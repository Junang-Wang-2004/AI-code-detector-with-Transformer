v1 = int(input())
v2, v3, v4 = ([], [], [])
for v5 in range(v1 - 1):
    v6 = [int(v5) for v5 in input().split()]
    v2.append(v6[0])
    v3.append(v6[1])
    v4.append(v6[2])
for v7 in range(v1):
    v8 = 0
    for v9 in range(v7, v1 - 1):
        if v8 < v3[v9]:
            v8 = v3[v9] + v2[v9]
        else:
            v8 = ((v8 - 1) // v4[v9] + 1) * v4[v9] + v2[v9]
    print(v8)
