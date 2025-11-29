class C1(object):

    def maxConsecutive(self, a1, a2, a3):
        """
        """
        a3.sort()
        v1 = max(a3[0] - a1, a2 - a3[-1])
        for v2 in range(1, len(a3)):
            v1 = max(v1, a3[v2] - a3[v2 - 1] - 1)
        return v1
