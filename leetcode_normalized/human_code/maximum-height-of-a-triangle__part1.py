class C1(object):

    def maxHeightOfTriangle(self, a1, a2):
        """
        """

        def f(a1, a2):
            v1, v2 = (int(2 * a1 ** 0.5) - 1, int((4 * a2 + 1) ** 0.5) - 1)
            return min(v1, v2) + int(v1 != v2)
        return max(f(a1, a2), f(a2, a1))
