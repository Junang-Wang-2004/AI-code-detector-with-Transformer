class C1(object):

    def minimumPerimeter(self, a1):
        """
        """
        v1 = int((2 * a1) ** (1.0 / 3))
        v1 -= v1 % 2
        assert (v1 - 2) * (v1 - 1) * v1 < 2 * a1 < (v1 + 2) ** 3
        v1 += 2
        if (v1 - 2) * (v1 - 1) * v1 < 2 * a1:
            v1 += 2
        return 8 * (v1 - 2) // 2
