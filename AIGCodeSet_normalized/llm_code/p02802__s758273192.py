v1 = input().split()
v2 = int(v1[0])
v3 = int(v1[1])
v4 = {}
v5 = 0
v6 = 0
for v7 in range(v3):
    v1 = input().split()
    v8 = int(v1[0])
    v9 = str(v1[1])
    v10 = v4.get(v8, None)
    if v9 == 'AC' and v10 != 'AC':
        v5 += 1
        v4[v8] = 'AC'
    if v9 == 'WA' and v10 != 'AC':
        v6 += 1
print(f'{v5} {v6}')
