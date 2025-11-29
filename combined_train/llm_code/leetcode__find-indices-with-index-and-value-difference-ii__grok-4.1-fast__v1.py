class C1(object):

    def findIndices(self, a1, a2, a3):
        v1 = len(a1)
        if v1 < a2 + 1:
            return [-1, -1]
        v2 = [0] * v1
        v3 = [0] * v1
        v2[v1 - 1] = v1 - 1
        v3[v1 - 1] = v1 - 1
        for v4 in range(v1 - 2, -1, -1):
            if a1[v4] < a1[v2[v4 + 1]]:
                v2[v4] = v4
            else:
                v2[v4] = v2[v4 + 1]
            if a1[v4] > a1[v3[v4 + 1]]:
                v3[v4] = v4
            else:
                v3[v4] = v3[v4 + 1]
        for v5 in range(v1 - a2):
            v6 = v5 + a2
            if a1[v5] - a1[v2[v6]] >= a3:
                return [v5, v2[v6]]
            if a1[v3[v6]] - a1[v5] >= a3:
                return [v5, v3[v6]]
        return [-1, -1]
