class C1(object):

    def maxScore(self, a1):
        """
        """
        v1, v2, v3 = (0, 0, 0)
        for v4 in range(1, len(a1) - 1):
            if a1[v4] == '0':
                v2 += 1
            else:
                v3 += 1
            v1 = max(v1, v2 - v3)
        return v1 + v3 + (a1[0] == '0') + (a1[-1] == '1')
