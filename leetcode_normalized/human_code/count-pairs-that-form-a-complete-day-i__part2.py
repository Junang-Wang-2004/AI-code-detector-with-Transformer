class C1(object):

    def countCompleteDayPairs(self, a1):
        """
        """
        return sum(((a1[i] + a1[j]) % 24 == 0 for v1 in range(len(a1) - 1) for v2 in range(v1 + 1, len(a1))))
