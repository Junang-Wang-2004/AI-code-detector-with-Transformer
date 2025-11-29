class C1(object):

    def minOperationsToMakeMedianK(self, a1, a2):
        """
        """
        a1.sort()
        return sum((max(a1[i] - a2, 0) for v1 in range(len(a1) // 2 + 1))) + sum((max(a2 - a1[v1], 0) for v1 in range(len(a1) // 2, len(a1))))
