class C1(object):

    def maximumNumberOfOnes(self, a1, a2, a3, a4):
        """
        """
        if a1 < a2:
            a1, a2 = (a2, a1)
        v3, v4 = divmod(a2, a3)
        v5, v6 = divmod(a1, a3)
        assert v3 <= v5
        v7 = [(v4 * v6, (v3 + 1) * (v5 + 1)), (v4 * (a3 - v6), (v3 + 1) * v5), ((a3 - v4) * v6, v3 * (v5 + 1)), ((a3 - v4) * (a3 - v6), v3 * v5)]
        v8 = 0
        for v9, v10 in v7:
            v9 = min(a4, v9)
            v8 += v10 * v9
            a4 -= v9
            if not a4:
                break
        return v8
