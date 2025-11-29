class C1(object):

    def maximumSum(self, a1):
        """
        """
        return max((sum((a1[i * x ** 2 - 1] for v1 in range(1, int((len(a1) // i) ** 0.5) + 1))) for v2 in range(1, len(a1) + 1)))
