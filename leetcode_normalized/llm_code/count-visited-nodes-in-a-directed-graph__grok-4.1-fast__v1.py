class C1:

    def countVisitedNodes(self, a1):
        v1 = len(a1)
        v2 = [0] * v1
        v3 = [False] * v1
        for v4 in range(v1):
            if v3[v4]:
                continue
            v5 = []
            v6 = set()
            v7 = v4
            while True:
                if v3[v7]:
                    v8 = v2[v7]
                    for v9 in range(len(v5) - 1, -1, -1):
                        v8 += 1
                        v2[v5[v9]] = v8
                    break
                if v7 in v6:
                    v10 = v5.index(v7)
                    v11 = len(v5) - v10
                    for v9 in range(v10, len(v5)):
                        v2[v5[v9]] = v11
                    v8 = v11
                    for v9 in range(v10 - 1, -1, -1):
                        v8 += 1
                        v2[v5[v9]] = v8
                    break
                v6.add(v7)
                v5.append(v7)
                v7 = a1[v7]
            for v12 in v5:
                v3[v12] = True
        return v2
