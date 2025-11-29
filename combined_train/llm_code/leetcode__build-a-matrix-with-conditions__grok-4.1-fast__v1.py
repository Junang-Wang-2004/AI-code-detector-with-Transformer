class C1(object):

    def buildMatrix(self, a1, a2, a3):

        def compute_order(a1):
            v1 = [[] for v2 in range(a1)]
            v3 = [0] * a1
            for v4, v5 in a1:
                v6 = v4 - 1
                v7 = v5 - 1
                v1[v6].append(v7)
                v3[v7] += 1
            v8 = [i for v9 in range(a1) if v3[v9] == 0]
            v10 = []
            while v8:
                v11 = v8.pop(0)
                v10.append(v11)
                for v12 in v1[v11]:
                    v3[v12] -= 1
                    if v3[v12] == 0:
                        v8.append(v12)
            return v10
        v1 = compute_order(a2)
        if len(v1) != a1:
            return []
        v2 = compute_order(a3)
        if len(v2) != a1:
            return []
        v3 = [0] * a1
        v4 = [0] * a1
        for v5, v6 in enumerate(v1):
            v3[v6] = v5
        for v5, v6 in enumerate(v2):
            v4[v6] = v5
        v7 = [[0] * a1 for v8 in range(a1)]
        for v9 in range(1, a1 + 1):
            v10 = v9 - 1
            v7[v3[v10]][v4[v10]] = v9
        return v7
