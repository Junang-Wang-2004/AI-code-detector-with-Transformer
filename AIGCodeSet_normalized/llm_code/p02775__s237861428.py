v1 = input()
v2 = len(v1)
v3 = v1[::-1] + '0'
v4 = False
v5 = 0
v6 = 0
for v7 in range(v2 - 1):
    v8 = int(v3[v7]) + v6
    v9 = int(v3[v7 + 1])
    if not v4:
        if v8 < 5 or (v8 == 5 and v9 < 5):
            v5 += v8
            v6 = 0
            v10 = 0
            continue
        v4 = True
        v10 = 10 - v8
        v6 += 1
        continue
    if v8 < 5:
        v5 += v10 + v8
        v6 = 0
        v4 = False
    elif v8 > 5:
        v10 += 10 - v8
    elif v9 < 5:
        v5 += v10 + v8
        v6 = 0
        v4 = False
    else:
        v10 += 10 - v8
v11 = int(v1[0]) + v6
v5 += v10 + min(v11, 11 - v11)
print(v5)
