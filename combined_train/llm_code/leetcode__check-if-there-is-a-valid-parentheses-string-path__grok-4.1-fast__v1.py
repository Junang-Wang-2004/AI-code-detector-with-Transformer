class C1:

    def hasValidPath(self, a1):
        v1, v2 = (len(a1), len(a1[0]))
        if (v1 + v2 - 1) % 2 != 0:
            return False
        v3 = [set() for v4 in range(v2)]
        v5 = 1 if a1[0][0] == '(' else -1
        if v5 >= 0:
            v3[0].add(v5)
        for v6 in range(1, v2):
            v5 = 1 if a1[0][v6] == '(' else -1
            v7 = set()
            for v8 in v3[v6 - 1]:
                v9 = v8 + v5
                if v9 >= 0:
                    v7.add(v9)
            v3[v6] = v7
        for v10 in range(1, v1):
            v11 = [set() for v4 in range(v2)]
            v5 = 1 if a1[v10][0] == '(' else -1
            v7 = set()
            for v8 in v3[0]:
                v9 = v8 + v5
                if v9 >= 0:
                    v7.add(v9)
            v11[0] = v7
            for v6 in range(1, v2):
                v5 = 1 if a1[v10][v6] == '(' else -1
                v7 = set()
                for v8 in v11[v6 - 1]:
                    v9 = v8 + v5
                    if v9 >= 0:
                        v7.add(v9)
                for v8 in v3[v6]:
                    v9 = v8 + v5
                    if v9 >= 0:
                        v7.add(v9)
                v11[v6] = v7
            v3 = v11
        return 0 in v3[v2 - 1]
