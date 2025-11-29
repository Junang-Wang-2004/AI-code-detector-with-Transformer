class C1(object):

    def countCompleteDayPairs(self, a1):
        """
        """
        v1 = 0
        v2 = [0] * 24
        for v3 in a1:
            v1 += v2[-v3 % 24]
            v2[v3 % 24] += 1
        return v1
