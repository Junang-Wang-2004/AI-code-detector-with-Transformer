v1 = int(input())
v2 = [v1 - i for v3 in range(v1)]
if v1 == 2:
    print('Yes')
    print(2)
    print(2, 1, 2)
    print(2, 1, 2)
    exit()
v1 *= 2
v4 = -int(-v1 ** 0.5 // 1)
if v1 / v4 == v1 // v4:
    v5 = v1 // v4
else:
    print('No')
    exit()
v6 = [[0 for v7 in range(v5)] for v3 in range(v4)]
for v3 in range(v1 - 1):
    for v7 in range(v3, v5):
        v8 = v2.pop(-1)
        v6[v3][v7] = v8
        v6[v7 + 1][v3] = v8
print('Yes')
print(len(v6))
for v9 in v6:
    print(len(v9), *v9)
