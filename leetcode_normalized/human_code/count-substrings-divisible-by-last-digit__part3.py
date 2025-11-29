class C1(object):

    def countSubstrings(self, a1):
        """
        """
        v1 = 0
        v2 = [[0] * 10 for v3 in range(10)]
        for v4 in range(1, len(a1) + 1):
            v5 = [[0] * 10 for v3 in range(10)]
            v6 = ord(a1[v4 - 1]) - ord('0')
            for v7 in range(1, 9 + 1):
                v5[v7][v6 % v7] += 1
                for v8 in range(v7):
                    v5[v7][(v8 * 10 + v6) % v7] += v2[v7][v8]
            v2 = v5
            v1 += v2[v6][0]
        return v1
