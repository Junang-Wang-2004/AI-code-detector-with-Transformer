class C1(object):

    def countWays(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        a1.sort()
        v2 = 0
        v3 = float('-inf')
        for v4, v5 in a1:
            if v4 > v3:
                v2 += 1
            v3 = max(v3, v5)
        return pow(2, v2, v1)
