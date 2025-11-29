class C1(object):

    def minPairSum(self, a1):
        """
        """
        a1.sort()
        return max((a1[i] + a1[-1 - i] for v1 in range(len(a1) // 2)))
