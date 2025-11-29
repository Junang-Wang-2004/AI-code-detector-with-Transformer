import sys
input = sys.stdin.readline
v1, v2, v3 = map(int, input().split())
v4 = [tuple(map(int, input().split())) for v5 in range(v3)]
v4.sort()
v6 = [0]
v7 = v6.append
for v5 in range(1, v3):
    if v4[v5][0] != v4[v5 - 1][0]:
        v7(v5)
if v3 > 0:
    v7(v3)
v8 = tuple((v4[b][0] for v9 in v6 if v9 < v3))
v10 = tuple((tuple((v4[j][1] for v11 in range(v6[v5], v6[v5 + 1]))) for v5 in range(len(v6) - 1)))
v12 = len(v10)
v13 = [[[False] * 3 for v14 in range(3)] for v11 in range(len(v10[0]) if 0 < v12 else 0)]
v15 = [[[False] * 3 for v14 in range(3)] for v11 in range(len(v10[1]) if 1 < v12 else 0)]
v16 = [[[False] * 3 for v14 in range(3)] for v11 in range(len(v10[2]) if 2 < v12 else 0)]
v17 = dict(zip(v10[0], list(range(len(v10[0]))))) if 0 < v12 else {}
v18 = dict(zip(v10[1], list(range(len(v10[1]))))) if 1 < v12 else {}
v19 = dict(zip(v10[2], list(range(len(v10[2]))))) if 2 < v12 else {}
v20 = [0] * 9
v21 = [[1] * 3 for v5 in range(3)]
v22 = [0] * 12
for v23 in range(v12):
    v24 = len(v10[v23])
    v25 = v8[v23]
    if v23 != 0:
        v13 = v15
        v17 = v18
        v15 = v16
        v18 = v19
        if v23 < v12 - 2:
            v26 = range(len(v10[v23 + 2]))
            v16 = [[[False] * 3 for v14 in range(3)] for v11 in v26]
            v19 = dict(zip(v10[v23 + 2], list(v26)))
    if v8[v23 + 1] is v25 + 1 if v23 < v12 - 1 else False:
        v27 = v25 + 1
        if v8[v23 + 2] is v25 + 2 if v23 < v12 - 2 else False:
            v28 = v25 + 2
        else:
            v28 = None
    elif v8[v23 + 1] is v25 + 2 if v23 < v12 - 1 else False:
        v27 = v25 + 2
        v28 = None
    else:
        v27 = None
        v28 = None
    for v29 in range(v24):
        v30 = v10[v23][v29]
        v31 = v13[v29]
        v32 = []
        v33 = []
        v34 = []
        for v35 in range(3):
            if not v31[0][v35]:
                if v30 - 2 + v35 >= 1 and v30 + v35 <= v2 and (v25 - 2 >= 1) and (v25 <= v1):
                    v32.append(v35)
                else:
                    v31[0][v35] = True
            if not v31[1][v35]:
                if v30 - 2 + v35 >= 1 and v30 + v35 <= v2 and (v25 - 2 + 1 >= 1) and (v25 + 1 <= v1):
                    v33.append(v35)
                else:
                    v31[1][v35] = True
            if not v31[2][v35]:
                if v30 - 2 + v35 >= 1 and v30 + v35 <= v2 and (v25 - 2 + 2 >= 1) and (v25 + 2 <= v1):
                    v34.append(v35)
                else:
                    v31[2][v35] = True
        v36 = []
        v37 = v36.append
        v38 = 0
        if v30 + 1 in v17 if v30 + 1 <= v2 else False:
            v37((v25, v30 + 1))
            v22[v38] = v17[v30 + 1]
            v38 += 1
        if v30 + 2 in v17 if v30 + 2 <= v2 else False:
            v37((v25, v30 + 2))
            v22[v38] = v17[v30 + 2]
            v38 += 1
        if v27 <= v1 if v27 is not None else False:
            for v39 in range(max(v30 - 2, 1), min(v30 + 3, v2 + 1)):
                if v39 in v18:
                    v37((v27, v39))
                    v22[v38] = v18[v39]
                    v38 += 1
        if v28 <= v1 if v28 is not None else False:
            for v39 in range(max(v30 - 2, 1), min(v30 + 3, v2 + 1)):
                if v39 in v19:
                    v37((v28, v39))
                    v22[v38] = v19[v39]
                    v38 += 1
        for v5, (v40, v41) in enumerate(v36):
            if v40 is v25:
                v42 = 0
                v43 = v22[v5]
            elif v40 is v27:
                v42 = 1
                v43 = v22[v5]
            elif v40 is v28:
                v42 = 2
                v43 = v22[v5]
            for v44 in range(v40 - v25, 3):
                for v35 in range(max(v41 - v30, 0), min(3, 3 + v41 - v30)):
                    if not v31[v44][v35]:
                        v21[v44][v35] += 1
                        if v42 is 0:
                            v13[v43][v44 - v40 + v25][v35 - v41 + v30] = True
                        elif v42 is 1:
                            v15[v43][v44 - v40 + v25][v35 - v41 + v30] = True
                        else:
                            v16[v43][v44 - v40 + v25][v35 - v41 + v30] = True
        for v44 in range(3):
            for v35 in range(3):
                if not v31[v44][v35]:
                    v20[v21[v44][v35] - 1] += 1
                    v21[v44][v35] = 1
print((v2 - 2) * (v1 - 2) - sum(v20))
for v5 in range(9):
    print(v20[v5])
