class C1(object):

    def maxA(self, a1):
        if a1 <= 6:
            return a1
        v1, v2, v3, v4, v5 = (2, 3, 4, 5, 6)
        for v6 in range(a1 - 6):
            v7 = max(v2 * 3, v1 * 4)
            v1, v2, v3, v4, v5 = (v2, v3, v4, v5, v7)
        return v5
