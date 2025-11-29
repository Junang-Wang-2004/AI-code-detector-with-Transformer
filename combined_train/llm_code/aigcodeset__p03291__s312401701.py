v1 = dict()
v1['A'] = []
v1['B'] = []
v1['C'] = []
v1['?'] = []
v2 = input()
for v3 in range(0, len(v2)):
    v4 = v2[v3]
    v1[v4].append(v3)
v5 = 0
v6 = [0] * 4
v7 = 10 ** 9 + 7
v6[0] = 1
for v8 in v2:
    if v8 == '?':
        for v3 in range(3, 0, -1):
            v6[v3] = (v6[v3] * 3 + v6[v3 - 1]) % v7
        v6[0] = v6[0] * 3 % v7
    elif v8 == 'A':
        v6[1] = (v6[1] + v6[0]) % v7
    elif v8 == 'B':
        v6[2] = (v6[2] + v6[1]) % v7
    elif v8 == 'C':
        v6[3] = (v6[3] + v6[2]) % v7
print(v6[3] % v7)
