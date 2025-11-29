class C1(object):

    def maximumCost(self, a1, a2, a3):
        """
        """
        if a3 + 1 > a1:
            return -1
        v1 = [[] for v2 in range(a1)]
        for v3, v4, v5 in a2:
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5))
        v6 = -1
        v7 = [(u, 1 << u, 0) for v8 in range(a1)]
        while v7:
            v9 = []
            for v8, v10, v11 in v7:
                if bin(v10).count('1') == a3 + 1:
                    v6 = max(v6, v11)
                for v12, v5 in v1[v8]:
                    if v10 & 1 << v12 == 0:
                        v9.append((v12, v10 | 1 << v12, v11 + v5))
            v7 = v9
        return v6
