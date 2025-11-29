class C1(object):

    def largestLocal(self, a1):
        """
        """

        def find_max(a1, a2):
            return max((a1[ni][nj] for v1 in range(a1, a1 + 3) for v2 in range(a2, a2 + 3)))
        return [[find_max(i, j) for v1 in range(len(a1[0]) - 2)] for v2 in range(len(a1) - 2)]
