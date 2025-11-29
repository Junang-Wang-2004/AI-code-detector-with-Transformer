v1, v2 = list(map(int, input().split()))
v3 = dict()
v4 = 0
v5 = 0
v6 = dict()
for v7 in range(v2):
    v8, v9 = input().split()
    v8 = int(v8)
    if v8 not in v3:
        v3[v8] = 0
        v6[v8] = 0
    if v9 == 'AC' and v3[v8] == 0:
        v3[v8] = 1
        v4 += 1
    elif v9 == 'WA' and v3[v8] != 1:
        v3[v8] = 0
        v6[v8] += 1
    elif v3[v8] == 1:
        pass
for v10 in v3.keys():
    if v3[v10] == 1:
        v5 += v6[v10]
print('{0} {1}'.format(v4, v5))
