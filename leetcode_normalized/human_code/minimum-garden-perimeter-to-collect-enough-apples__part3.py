class C1(object):

    def minimumPerimeter(self, a1):
        """
        """

        def check(a1, a2):
            return r * (2 * r + 1) * (2 * r + 2) >= a1
        v1, v2 = (1, int((a1 / 4.0) ** (1.0 / 3)))
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if check(a1, v3):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return 8 * v1
