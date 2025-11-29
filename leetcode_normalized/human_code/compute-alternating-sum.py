class C1(object):

    def alternatingSum(self, a1):
        """
        """
        return sum((a1[i] for v1 in range(0, len(a1), 2))) - sum((a1[v1] for v1 in range(1, len(a1), 2)))
