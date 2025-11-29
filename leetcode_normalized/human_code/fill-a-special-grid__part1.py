class C1(object):

    def specialGrid(self, a1):
        """
        """

        def copy(a1, a2, a3, a4, a5):
            for v1 in range(a1):
                for v2 in range(a1):
                    result[a4 + v1][a5 + v2] = result[a2 + v1][a3 + v2] + a1 * a1
        v1 = 1 << a1
        v2 = [[0] * v1 for v3 in range(v1)]
        v4 = 1
        for v5 in range(a1):
            v6, v7 = (0, v1 - v4)
            for v8, v9 in ((v4, 0), (0, -v4), (-v4, 0)):
                v10, v11 = (v6 + v8, v7 + v9)
                copy(v4, v6, v7, v10, v11)
                v6, v7 = (v10, v11)
            v4 <<= 1
        return v2
