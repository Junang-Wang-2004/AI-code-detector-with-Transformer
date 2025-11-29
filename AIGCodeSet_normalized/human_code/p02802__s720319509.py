v1, v2 = map(int, input().split())
v3 = []
v4 = []
for v5 in range(v2):
    v6, v7 = input().split()
    v3.append(int(v6))
    v4.append(v7)
v8 = [0] * v1
v9 = [0] * v1
for v5 in range(v2):
    if v4[v5] == 'AC':
        v8[v3[v5] - 1] = 1
    if v8[v3[v5] - 1] != 1 and v4[v5] == 'WA':
        v9[v3[v5] - 1] += 1
for v5 in range(v1):
    if v8[v5] != 1 and v9[v5] > 0:
        v9[v5] = 0
print(str(sum(v8)) + ' ' + str(sum(v9)))
