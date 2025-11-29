class C1(object):

    def findPoisonedDuration(self, a1, a2):
        """
        """
        v1 = a2 * len(a1)
        for v2 in range(1, len(a1)):
            v1 -= max(0, a2 - (a1[v2] - a1[v2 - 1]))
        return v1
