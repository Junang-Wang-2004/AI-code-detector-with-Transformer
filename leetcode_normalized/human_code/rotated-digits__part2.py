class C1(object):

    def rotatedDigits(self, a1):
        """
        """
        v1, v2, v3 = (0, 1, 2)
        v4, v5 = ([0, 1, 8], [2, 5, 6, 9])
        v6 = [0] * (a1 + 1)
        v6[0] = v2
        for v7 in range(a1 // 10 + 1):
            if v6[v7] != v1:
                for v8 in v4:
                    if v7 * 10 + v8 <= a1:
                        v6[v7 * 10 + v8] = max(v2, v6[v7])
                for v8 in v5:
                    if v7 * 10 + v8 <= a1:
                        v6[v7 * 10 + v8] = v3
        return v6.count(v3)
