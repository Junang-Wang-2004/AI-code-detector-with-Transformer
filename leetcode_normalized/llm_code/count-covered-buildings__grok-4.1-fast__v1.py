class C1(object):

    def countCoveredBuildings(self, a1, a2):
        v1 = {}
        v2 = {}
        v3 = {}
        v4 = {}
        for v5 in a2:
            v6, v7 = (v5[0] - 1, v5[1] - 1)
            v1[v7] = min(v1.get(v7, a1), v6)
            v2[v7] = max(v2.get(v7, -1), v6)
            v3[v6] = min(v3.get(v6, a1), v7)
            v4[v6] = max(v4.get(v6, -1), v7)
        v8 = 0
        for v5 in a2:
            v6, v7 = (v5[0] - 1, v5[1] - 1)
            if v1[v7] < v6 < v2[v7] and v3[v6] < v7 < v4[v6]:
                v8 += 1
        return v8
