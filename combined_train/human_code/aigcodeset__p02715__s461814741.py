def f1(a1):
    if a1 == 1:
        raise ValueError('error!')
    v1 = 2
    while v1 * v1 <= a1:
        if a1 % v1 == 0:
            return False
        v1 += 1
    return True
v1, v2 = list(map(int, input().split()))
v3 = 10 ** 9 + 7
v4 = [-1] * (v2 + 1)
for v5 in range(v2 + 1):
    v4[v5] = pow(v5, v1, v3)
v6 = []
for v5 in range(2, v2 + 1):
    if f1(v5):
        v6.append(v5)
v7 = []
v8 = []
v9 = []
v10 = []
v11 = []
v12 = len(v6)
for v5, v13 in enumerate(v6):
    for v14 in range(v5 + 1, v12):
        v15 = v6[v14]
        if v13 * v15 > v2:
            break
        v7.append(v13 * v15)
        for v16 in range(v14 + 1, v12):
            v17 = v6[v16]
            if v13 * v15 * v17 > v2:
                break
            v8.append(v13 * v15 * v17)
            for v18 in range(v16 + 1, v12):
                v19 = v6[v18]
                if v13 * v15 * v17 * v19 > v2:
                    break
                v9.append(v13 * v15 * v17 * v19)
                for v20 in range(v18 + 1, v12):
                    v21 = v6[v20]
                    if v13 * v15 * v17 * v19 * v21 > v2:
                        break
                    v10.append(v13 * v15 * v17 * v19 * v21)
                    for v22 in range(v20 + 1, v12):
                        v23 = v6[v22]
                        if v13 * v15 * v17 * v19 * v21 * v23 > v2:
                            break
                        v11.append(v13 * v15 * v17 * v19 * v21 * v23)
v7.sort()
v8.sort()
v9.sort()
v10.sort()
v11.sort()
v24 = 0
v25 = 0
for v26 in range(1, v2 + 1):
    v27 = v2 // v26
    v28 = v4[v27]
    for v29 in v6:
        if v29 > v27:
            break
        v28 -= v4[v27 // v29]
    for v29 in v7:
        if v29 > v27:
            break
        v28 += v4[v27 // v29]
    for v29 in v8:
        if v29 > v27:
            break
        v28 -= v4[v27 // v29]
    for v29 in v9:
        if v29 > v27:
            break
        v28 += v4[v27 // v29]
    for v29 in v10:
        if v29 > v27:
            break
        v28 -= v4[v27 // v29]
    for v29 in v11:
        if v29 > v27:
            break
        v28 += v4[v27 // v29]
    v28 %= v3
    v24 += v26 * v28
    v25 += v28
print(v24 % v3)
