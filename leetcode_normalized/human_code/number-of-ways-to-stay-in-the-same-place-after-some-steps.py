class C1(object):

    def numWays(self, a1, a2):
        """
        """
        v1 = int(1000000000.0 + 7)
        v2 = min(1 + a1 // 2, a2)
        v3 = [0] * (v2 + 2)
        v3[1] = 1
        while a1 > 0:
            a1 -= 1
            v5 = [0] * (v2 + 2)
            for v6 in range(1, v2 + 1):
                v5[v6] = (v3[v6] + v3[v6 - 1] + v3[v6 + 1]) % v1
            v3 = v5
        return v3[1]
