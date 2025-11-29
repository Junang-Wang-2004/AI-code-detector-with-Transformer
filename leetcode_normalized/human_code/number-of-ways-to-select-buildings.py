class C1(object):

    def numberOfWays(self, a1):
        """
        """
        v1 = 3
        v2 = [[0] * 2 for v3 in range(v1)]
        for v4 in a1:
            v5 = ord(v4) - ord('0')
            v2[0][v5] += 1
            for v6 in range(1, len(v2)):
                v2[v6][v5] += v2[v6 - 1][1 ^ v5]
        return v2[-1][0] + v2[-1][1]
