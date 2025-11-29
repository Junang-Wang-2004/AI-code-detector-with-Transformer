v1 = str(input())
v2 = 0
for v3 in range(2 ** (len(v1) - 1)):
    v4 = []
    for v5 in range(len(v1)):
        v6 = 2 ** v5
        if v3 & v6 > 0:
            v4.append(v5)
    if len(v4) == 0:
        v7 = [int(v1)]
    else:
        v8 = 0
        v7 = []
        for v9 in v4:
            v7.append(int(v1[v8:v9 + 1]))
            v8 = v9 + 1
        v7.append(int(v1[v8:]))
    v2 += sum(v7)
print(v2)
