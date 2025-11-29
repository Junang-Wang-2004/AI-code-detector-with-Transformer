class C1(object):

    def rowAndMaximumOnes(self, a1):
        """
        """
        return max(([i, a1[i].count(1)] for v1 in range(len(a1))), key=lambda x: x[1])
