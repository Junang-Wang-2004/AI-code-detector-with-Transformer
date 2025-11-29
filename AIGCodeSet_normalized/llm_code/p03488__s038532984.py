v1 = input()
v2, v3 = map(int, input().split())
v4 = [0]
v5 = [0]
v6 = 0
while v1[v6] == 'F':
    v4[0] += 1
    if v6 == len(v1):
        break
v7 = 0
for v8 in range(v6, len(v1)):
    v9 = 0
    while v1[v8] == 'F':
        v8 += 1
        v9 += 1
        if v8 == len(v1):
            break
    v10 = set()
    if v7 == 0:
        for v6 in v4:
            v10.add(v6 + v9)
            v10.add(v6 - v9)
        v4 = []
        for v6 in v10:
            v4.append(v6)
    else:
        for v6 in v5:
            v10.add(v6 + v9)
            v10.add(v6 - v9)
        v5 = []
        for v6 in v10:
            v5.append(v6)
    v9 = 0
    while v1[v8] == 'T':
        v8 += 1
        v9 += 1
        if v8 == len(v1):
            break
    v7 = (v7 + v9) % 2
if v2 in v4 and v3 in v5:
    print('Yes')
else:
    print('No')
