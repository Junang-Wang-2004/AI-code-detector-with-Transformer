class C1(object):

    def maxHeightOfTriangle(self, a1, a2):
        """
        """

        def f(a1, a2):
            v1 = 0
            while a1 >= v1 + 1:
                v1 += 1
                a1 -= v1
                a1, a2 = (a2, a1)
            return v1
        return max(f(a1, a2), f(a2, a1))
