class C1(object):

    def getAverages(self, a1, a2):
        v1 = len(a1)
        v2 = [-1] * v1
        v3 = 2 * a2 + 1
        if v1 < v3:
            return v2
        v4 = sum(a1[:v3])
        v2[a2] = v4 // v3
        for v5 in range(a2 + 1, v1 - a2):
            v4 -= a1[v5 - a2 - 1]
            v4 += a1[v5 + a2]
            v2[v5] = v4 // v3
        return v2
