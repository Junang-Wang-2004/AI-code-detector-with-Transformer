class C1:

    def maxStudents(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = len(a1[0])
        v3 = sum((s.count('.') for v4 in a1))
        v5 = []
        v6 = []
        v7 = {}
        v8 = {}
        v9 = 0
        v10 = 0
        for v11 in range(v1):
            for v12 in range(v2):
                if a1[v11][v12] == '.':
                    if v12 % 2 == 0:
                        v5.append((v11, v12))
                        v7[v11, v12] = v9
                        v9 += 1
                    else:
                        v6.append((v11, v12))
                        v8[v11, v12] = v10
                        v10 += 1
        v13 = len(v5)
        v14 = len(v6)
        v15 = [[] for v16 in range(v13)]
        v17 = [(-1, -1), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 1)]
        for v18 in range(v13):
            v19, v20 = v5[v18]
            for v21, v22 in v17:
                v23, v24 = (v19 + v21, v20 + v22)
                if 0 <= v23 < v1 and 0 <= v24 < v2 and (a1[v23][v24] == '.') and (v24 % 2 == 1):
                    if (v23, v24) in v8:
                        v15[v18].append(v8[v23, v24])
        v25 = [-1] * v14
        v26 = [-1] * v13
        v27 = [False] * v14

        def find_path(a1):
            for v1 in v15[a1]:
                if v27[v1]:
                    continue
                v27[v1] = True
                if v25[v1] == -1 or find_path(v25[v1]):
                    v25[v1] = a1
                    v26[a1] = v1
                    return True
            return False
        v28 = 0
        for v18 in range(v13):
            if v26[v18] == -1:
                v27 = [False] * v14
                if find_path(v18):
                    v28 += 1
        return v3 - v28
