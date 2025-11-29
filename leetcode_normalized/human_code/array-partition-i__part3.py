class C1(object):

    def arrayPairSum(self, a1):
        """
        """
        a1 = sorted(a1)
        return sum([a1[i] for v2 in range(0, len(a1), 2)])
