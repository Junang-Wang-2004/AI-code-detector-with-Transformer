v1 = int(input())
v2, v3, v4 = ([], [], [])
for v5 in range(v1 - 1):
    v6, v7, v8 = tuple(map(int, input().split()))
    v2.append(v6)
    v3.append(v7)
    v4.append(v8)
for v9 in range(v1 - 1):
    v10 = 0
    for v11, (v6, v7, v8) in enumerate(zip(v2[v9:], v3[v9:], v4[v9:])):
        if v11 == 0:
            v10 += v6 + v7
        else:
            if v10 < v7:
                v10 = v7
            if v10 % v8 != 0:
                v10 += v8 - v10 % v8
            v10 += v6
    print(v10)
print(0)
