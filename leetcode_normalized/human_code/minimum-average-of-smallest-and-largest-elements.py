class C1(object):

    def minimumAverage(self, a1):
        """
        """
        a1.sort()
        return min(((a1[i] + a1[~i]) / 2.0 for v1 in range(len(a1) // 2)))
