class C1(object):

    def minCost(self, a1, a2, a3, a4, a5):
        """
        """
        v1 = {(0, 0): 0}
        for v2, v3 in enumerate(a1):
            v4 = {}
            for v5 in range(1, a4 + 1) if not v3 else [v3]:
                for v6, v7 in v1:
                    v8 = v6 + (v7 != v5)
                    if v8 > a5:
                        continue
                    v4[v8, v5] = min(v4.get((v8, v5), float('inf')), v1[v6, v7] + (a2[v2][v5 - 1] if v5 != v3 else 0))
            v1 = v4
        return min([v1[v6, v7] for v6, v7 in v1 if v6 == a5] or [-1])
