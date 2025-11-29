v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = 10 ** 9 + 7
v3.sort()
v5 = []
v6 = []
if v1 == v2:
    v7 = 1
    for v8 in v3:
        v7 *= v8
        v7 %= v4
    print(v7)
    exit()
for v8 in v3:
    if v8 < 0:
        v5.append(v8)
    else:
        v6.append(v8)
if v6 == []:
    v7 = 1
    v9 = 0
    if v2 % 2:
        while v9 < v2:
            v7 *= v3[-1 - v9]
            v7 %= v4
            v9 += 1
    else:
        while v9 < v2:
            v7 *= v3[v9]
            v7 %= v4
            v9 += 1
    print(v7)
    exit()
v6 = sorted(v6, reverse=True)
v10 = 0
v11 = 0
if v2 % 2:
    v9 = v6[0]
    v2 -= 1
    v10 += 1
else:
    v9 = 1
while v2 > 0:
    v12 = True
    v13 = True
    if v10 + 2 <= len(v6):
        v14 = v6[v10] * v6[v10 + 1]
    else:
        v14 = 1
        v12 = False
    if v11 + 2 <= len(v5):
        v15 = v5[v11] * v5[v11 + 1]
    else:
        v15 = 1
        v13 = False
    if v14 > v15 or (v12 and (not v13)):
        v10 += 2
        v9 = v14 * v9 % v4
    elif v13:
        v11 += 2
        v9 = v15 * v9 % v4
    if v12 == False and v13 == False:
        break
    v2 -= 2
print(v9 % v4)
