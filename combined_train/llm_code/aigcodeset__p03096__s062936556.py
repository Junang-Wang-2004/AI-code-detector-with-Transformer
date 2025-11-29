v1 = int(input())
v2 = []
for v3 in range(v1):
    v4 = int(input())
    if v3 == 0:
        v2.append(v4)
    elif v2[-1] != v4:
        v2.append(v4)
v1 = len(v2)
v5 = [0] * v1
v6 = {}
for v3 in range(v1):
    if v3 == 0:
        v6[v2[v3]] = v3
        v5[v3] = 1
    elif v2[v3] not in v6.keys():
        v5[v3] = v5[v3 - 1]
        v6[v2[v3]] = v3
    else:
        v5[v3] = (v5[v3 - 1] + v5[v6[v2[v3]]]) % (10 ** 9 + 7)
        v6[v2[v3]] = v3
print(v5[-1])
