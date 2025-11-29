class C1(object):

    def maxRotateFunction(self, a1):
        v1 = len(a1)
        v2 = 0
        v3 = 0
        for v4 in range(v1):
            v2 += a1[v4]
            v3 += v4 * a1[v4]
        v5 = v3
        for v6 in range(1, v1 + 1):
            v7 = a1[v1 - v6]
            v3 += v2 - v1 * v7
            v5 = max(v5, v3)
        return v5
