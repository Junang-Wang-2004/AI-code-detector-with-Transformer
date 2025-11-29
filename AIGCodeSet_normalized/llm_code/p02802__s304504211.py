v1, v2 = map(int, input().split())
v3 = [False] * v1
v4 = [0] * v1
for v5 in range(v2):
    v6, v7 = input().split()
    v6 = int(v6) - 1
    if v7 == 'AC':
        v3[v6] = True
    else:
        v4[v6] += 1
v8 = 0
v9 = 0
for v5 in range(v1):
    if v3[v5] == True:
        v8 += 1
        v9 += v4[v5]
print(v8, v9, sep=' ')
