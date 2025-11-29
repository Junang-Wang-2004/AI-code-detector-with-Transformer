class C1:

    def queryResults(self, a1, a2):
        v1 = {}
        v2 = {}
        v3 = [0] * len(a2)
        for v4, (v5, v6) in enumerate(a2):
            if v5 in v1:
                v7 = v1[v5]
                v2[v7] -= 1
                if v2[v7] == 0:
                    del v2[v7]
            v1[v5] = v6
            if v6 not in v2:
                v2[v6] = 0
            v2[v6] += 1
            v3[v4] = len(v2)
        return v3
