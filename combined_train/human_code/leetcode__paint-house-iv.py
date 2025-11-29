class C1(object):

    def minCost(self, a1, a2):
        """
        """
        v1 = len(a2[0])
        v2 = [[0] * v1 for v3 in range(v1)]
        for v4 in range(a1 // 2):
            v5 = [[float('inf')] * v1 for v3 in range(v1)]
            for v3 in range(v1):
                for v6 in range(v1):
                    if v6 == v3:
                        continue
                    for v7 in range(v1):
                        if v7 == v3:
                            continue
                        for v8 in range(v1):
                            if v8 == v6 or v7 == v8:
                                continue
                            v5[v7][v8] = min(v5[v7][v8], v2[v3][v6] + a2[v4][v7] + a2[~v4][v8])
            v2 = v5
        return min((v2[v3][v6] for v3 in range(v1) for v6 in range(v1) if v3 != v6))
