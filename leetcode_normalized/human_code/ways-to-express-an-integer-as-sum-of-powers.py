class C1(object):

    def numberOfWays(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [0] * (a1 + 1)
        v2[0] = 1
        for v3 in range(1, a1 + 1):
            v4 = v3 ** a2
            if v4 > a1:
                break
            for v5 in reversed(range(v4, a1 + 1)):
                v2[v5] = (v2[v5] + v2[v5 - v4]) % v1
        return v2[-1]
