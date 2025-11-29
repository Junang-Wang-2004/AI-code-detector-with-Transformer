class C1(object):

    def maxScore(self, a1):
        """
        """
        return sum(a1) - min(a1) if len(a1) % 2 else sum(a1) - min((a1[i] + a1[i + 1] for v1 in range(len(a1) - 1)))
