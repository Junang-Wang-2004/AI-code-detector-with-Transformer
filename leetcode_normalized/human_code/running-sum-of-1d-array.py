class C1(object):

    def runningSum(self, a1):
        """
        """
        for v1 in range(len(a1) - 1):
            a1[v1 + 1] += a1[v1]
        return a1
