class C1(object):

    def maxArea(self, a1, a2, a3, a4):
        """
        """

        def max_len(a1, a2):
            a2.sort()
            a1 = max(a2[0] - 0, a1 - a2[-1])
            for v2 in range(1, len(a2)):
                a1 = max(a1, a2[v2] - a2[v2 - 1])
            return a1
        v1 = 10 ** 9 + 7
        return max_len(a1, a3) * max_len(a2, a4) % v1
