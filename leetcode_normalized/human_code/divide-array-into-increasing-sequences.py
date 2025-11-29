class C1(object):

    def canDivideIntoSubsequences(self, a1, a2):
        """
        """
        v1, v2 = (1, 1)
        for v3 in range(1, len(a1)):
            v1 = 1 if a1[v3 - 1] < a1[v3] else v1 + 1
            v2 = max(v2, v1)
        return a2 * v2 <= len(a1)
