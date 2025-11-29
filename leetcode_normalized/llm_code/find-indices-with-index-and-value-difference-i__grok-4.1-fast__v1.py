class C1(object):

    def findIndices(self, a1, a2, a3):
        v1 = len(a1)
        v2 = 0
        v3 = 0
        for v4 in range(v1 - a2):
            if a1[v4] > a1[v2]:
                v2 = v4
            if a1[v4] < a1[v3]:
                v3 = v4
            v5 = v4 + a2
            if a1[v2] - a1[v5] >= a3:
                return [v2, v5]
            if a1[v5] - a1[v3] >= a3:
                return [v3, v5]
        return [-1, -1]
