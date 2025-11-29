class C1(object):

    def maximumScore(self, a1, a2, a3):
        """
        """
        return min((a1 + a2 + a3) // 2, a1 + a2 + a3 - max(a1, a2, a3))
