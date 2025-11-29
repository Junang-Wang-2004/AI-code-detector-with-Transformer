def f1(a1, a2):
    v1 = 0
    v2 = int(a2[0])
    for v3 in range(len(a2) - 1):
        if a1[v3] == '0':
            v2 = v2 * 10 + int(a2[v3 + 1])
        else:
            v1 += v2
            v2 = int(a2[v3 + 1])
    v1 += v2
    return v1
v1 = input()
v2 = [int(v1[i]) for v3 in range(len(v1))]
v4 = len(v1) - 1
v5 = '0' + str(v4) + 'b'
v6 = 0
for v3 in range(2 ** v4):
    v7 = format(v3, v5)
    v6 += f1(v7, v2)
print(v6)
