class C1(object):

    def minimumDifference(self, a1, a2):
        """
        """
        a1.sort()
        return min((a1[i] - a1[i - a2 + 1] for v1 in range(a2 - 1, len(a1))))
