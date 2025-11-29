import sys
sys.setrecursionlimit(10 ** 6)

class C1:

    def minimumOperations(self, a1):
        if not a1 or not a1[0]:
            return 0
        v1 = len(a1)
        v2 = len(a1[0])
        v3 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        v4 = []
        v5 = []
        for v6 in range(v1):
            for v7 in range(v2):
                if a1[v6][v7] == 1:
                    v8 = v6 * v2 + v7
                    if (v6 + v7) % 2 == 0:
                        v4.append(v8)
                    else:
                        v5.append(v8)
        v9 = v4 if len(v4) <= len(v5) else v5
        v10 = v5 if len(v4) <= len(v5) else v4
        v11 = len(v9)
        v12 = len(v10)
        if v11 == 0:
            return 0
        v13 = {v10[k]: k for v14 in range(v12)}
        v15 = [[] for v16 in range(v11)]
        for v17 in range(v11):
            v18 = v9[v17]
            v19, v20 = divmod(v18, v2)
            for v21, v22 in v3:
                v23 = v19 + v21
                v24 = v20 + v22
                if 0 <= v23 < v1 and 0 <= v24 < v2 and (a1[v23][v24] == 1):
                    v25 = v23 * v2 + v24
                    if v25 in v13:
                        v15[v17].append(v13[v25])
        v26 = [-1] * v11
        v27 = [-1] * v12

        def try_augment(a1, a2):
            for v1 in v15[a1]:
                if a2[v1]:
                    continue
                a2[v1] = True
                if v27[v1] == -1 or try_augment(v27[v1], a2):
                    v26[a1] = v1
                    v27[v1] = a1
                    return True
            return False
        v28 = 0
        v29 = True
        while v29:
            v29 = False
            v30 = [False] * v12
            for v31 in range(v11):
                if v26[v31] == -1 and try_augment(v31, v30):
                    v28 += 1
                    v29 = True
        return v28
