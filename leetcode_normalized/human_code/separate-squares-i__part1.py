class C1(object):

    def separateSquares(self, a1):
        """
        """
        v1 = []
        for v2, v3, v4 in a1:
            v1.append((v3, 1, v4))
            v1.append((v3 + v4, -1, v4))
        v1.sort(key=lambda e: e[0])
        v5 = v6 = 0.0
        v7 = v1[0][0]
        for v3, v8, v4 in v1:
            if v3 != v7:
                v5 += (v3 - v7) * v6
                v7 = v3
            v6 += v4 * v8
        v9 = v5 / 2.0
        v5 = v6 = 0.0
        v7 = v1[0][0]
        for v3, v8, v4 in v1:
            if v3 != v7:
                if v5 + (v3 - v7) * v6 >= v9:
                    break
                v5 += (v3 - v7) * v6
                v7 = v3
            v6 += v4 * v8
        return v7 + (v9 - v5) / v6
