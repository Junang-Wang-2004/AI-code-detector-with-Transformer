class C1(object):

    def maxAlternatingSum(self, a1):
        """
        """
        v1 = sorted((x ** 2 for v2 in a1))
        return sum(v1) - 2 * sum((v1[i] for v3 in range(len(v1) // 2)))
