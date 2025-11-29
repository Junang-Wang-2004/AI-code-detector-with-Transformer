class C1(object):

    def maxWeight(self, a1, a2, a3, a4):
        """
        """
        v1 = [[] for v2 in range(a1)]
        for v3, v4, v5 in a2:
            v1[v3].append((v4, v5))
        v6 = [{0} for v2 in range(a1)]
        for v2 in range(a3):
            v7 = [set() for v2 in range(a1)]
            for v8 in range(a1):
                for v9 in v6[v8]:
                    for v10, v5 in v1[v8]:
                        if v9 + v5 < a4:
                            v7[v10].add(v9 + v5)
            v6 = v7
        v11 = -1
        for v12 in v6:
            if v12:
                v11 = max(v11, max(v12))
        return v11
