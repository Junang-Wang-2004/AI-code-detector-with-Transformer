v1 = int(input())
v2 = list(map(int, input().split()))
v3 = list(map(int, input().split()))
v4 = list(map(int, input().split()))
v5 = []
v6 = []
v7 = []
for v8 in range(v1):
    v5.append([v2[v8], 0])
    v5.append([v3[v8], 1])
    v5.append([v4[v8], 2])
v5.sort()
v9, v10 = (0, 0)
for v8 in range(3 * v1):
    if v5[v8][1] == 1:
        if v8 != 0 and v8 != 3 * v1 - 1:
            if v5[v8][0] == v5[v8 - 1][0] and v5[v8 - 1][1] == 0:
                v6.append(v9 - 1)
            else:
                v6.append(v9)
            if v5[v8][0] == v5[v8 + 1][0] and v5[v8 + 1][1] == 2:
                v7.append(v1 - v10 - 1)
            else:
                v7.append(v1 - v10)
        else:
            v6.append(v9)
            v7.append(v1 - v10)
    if v5[v8][1] == 0:
        v9 += 1
    if v5[v8][1] == 2:
        v10 += 1
v11 = 0
for v8 in range(v1):
    v11 += v6[v8] * v7[v8]
print(v11)
