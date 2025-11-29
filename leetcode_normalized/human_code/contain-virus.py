class C1(object):

    def containVirus(self, a1):
        """
        """
        v1 = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def dfs(a1, a2, a3, a4, a5, a6, a7):
            if (a2, a3) in a4:
                return
            a4.add((a2, a3))
            a5[-1].add((a2, a3))
            for v1 in v1:
                v2, v3 = (a2 + v1[0], a3 + v1[1])
                if not (0 <= v2 < len(a1) and 0 <= v3 < len(a1[a2])):
                    continue
                if a1[v2][v3] == 1:
                    dfs(a1, v2, v3, a4, a5, a6, a7)
                elif a1[v2][v3] == 0:
                    a6[-1].add((v2, v3))
                    a7[-1] += 1
        v2 = 0
        while True:
            v3, v4, v5, v6 = (set(), [], [], [])
            for v7, v8 in enumerate(a1):
                for v9, v10 in enumerate(v8):
                    if v10 == 1 and (v7, v9) not in v3:
                        v4.append(set())
                        v5.append(set())
                        v6.append(0)
                        dfs(a1, v7, v9, v3, v4, v5, v6)
            if not v4:
                break
            v11 = v5.index(max(v5, key=len))
            for v12, v13 in enumerate(v4):
                if v12 == v11:
                    v2 += v6[v12]
                    for v7, v9 in v13:
                        a1[v7][v9] = -1
                    continue
                for v7, v9 in v13:
                    for v14 in v1:
                        v15, v16 = (v7 + v14[0], v9 + v14[1])
                        if not (0 <= v15 < len(a1) and 0 <= v16 < len(a1[v7])):
                            continue
                        if a1[v15][v16] == 0:
                            a1[v15][v16] = 1
        return v2
