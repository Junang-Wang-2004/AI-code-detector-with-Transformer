class C1(object):

    def countLatticePoints(self, a1):
        """
        """
        v1 = max((x + r for v2, v3, v4 in a1))
        v5 = max((y + v4 for v3, v6, v4 in a1))
        v7 = 0
        for v8 in range(v1 + 1):
            for v9 in range(v5 + 1):
                if any(((v8 - v2) ** 2 + (v9 - v6) ** 2 <= v4 ** 2 for v2, v6, v4 in a1)):
                    v7 += 1
        return v7
