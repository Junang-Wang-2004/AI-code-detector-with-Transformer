class C1(object):

    def spiralMatrixIII(self, a1, a2, a3, a4):
        """
        """
        v1, v2 = (a3, a4)
        v3 = [[v1, v2]]
        v4, v5, v6, v7 = (0, 1, 0, 0)
        while len(v3) < a1 * a2:
            v1, v2, v7 = (v1 + v4, v2 + v5, v7 + 1)
            if 0 <= v1 < a1 and 0 <= v2 < a2:
                v3.append([v1, v2])
            if v7 == v6 // 2 + 1:
                v4, v5, v6, v7 = (v5, -v4, v6 + 1, 0)
        return v3
