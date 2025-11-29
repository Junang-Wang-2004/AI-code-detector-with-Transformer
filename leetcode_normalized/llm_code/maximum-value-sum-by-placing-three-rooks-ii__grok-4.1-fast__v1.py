class C1(object):

    def maximumValueSum(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = len(a1[0])
        v3 = 3
        v4 = set()
        for v5 in range(v1):
            v6 = [(a1[v5][j], v5, j) for v7 in range(v2)]
            v8 = sorted(v6, reverse=True)[:v3]
            for v9 in v8:
                v4.add(v9)
        v10 = set()
        for v7 in range(v2):
            v11 = [(a1[v5][v7], v5, v7) for v5 in range(v1)]
            v12 = sorted(v11, reverse=True)[:v3]
            for v9 in v12:
                v10.add(v9)
        v13 = v4 & v10
        v14 = sorted(v13, reverse=True)
        v15 = (v3 - 1) * (2 * v3 - 1) + 1
        v16 = v14[:v15]
        v17 = [False] * v1
        v18 = [False] * v2
        v19 = float('-inf')

        def search(a1, a2, a3):
            nonlocal res
            if a2 == v3:
                v1 = max(v1, a3)
                return
            for v2 in range(a1, len(v16)):
                v3, v4, v5 = v16[v2]
                if v17[v4] or v18[v5]:
                    continue
                v17[v4] = True
                v18[v5] = True
                search(v2 + 1, a2 + 1, a3 + v3)
                v17[v4] = False
                v18[v5] = False
        search(0, 0, 0)
        return v19
