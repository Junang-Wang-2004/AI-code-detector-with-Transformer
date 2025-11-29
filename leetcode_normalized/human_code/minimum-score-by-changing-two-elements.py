class C1(object):

    def minimizeSum(self, a1):
        """
        """
        a1.sort()
        return min((a1[-3 + i] - a1[i] for v1 in range(3)))
