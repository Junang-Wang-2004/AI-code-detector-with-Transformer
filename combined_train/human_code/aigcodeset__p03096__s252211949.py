v1 = int(input())
v2 = []
v3 = 10 ** 9 + 7
for v4 in range(v1):
    v5 = int(input())
    if v4 == 0:
        v2.append(v5)
    elif v2[-1] != v5:
        v2.append(v5)
v1 = len(v2)
v6 = [0] * v1
v7 = {}
for v4 in range(v1):
    if v4 == 0:
        v7[v2[v4]] = v4
        v6[v4] = 1
    elif v2[v4] not in v7:
        v6[v4] = v6[v4 - 1]
        v7[v2[v4]] = v4
    else:
        v6[v4] = v6[v4 - 1] + v6[v7[v2[v4]]]
        v7[v2[v4]] = v4
print(v6[-1] % v3)
