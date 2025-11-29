import math

class C1(object):

    def minimumPerimeter(self, a1):
        """
        """
        v1, v2, v3, v4 = (4.0, 6.0, 2.0, float(-a1))
        v5 = (3 * v1 * v3 - v2 ** 2) / (3 * v1 ** 2)
        v6 = (2 * v2 ** 3 - 9 * v1 * v2 * v3 + 27 * v1 ** 2 * v4) / (27 * v1 ** 3)
        assert (v6 / 2) ** 2 + (v5 / 3) ** 3 > 0
        v7 = (-v6 / 2 + ((v6 / 2) ** 2 + (v5 / 3) ** 3) ** 0.5) ** (1.0 / 3) + (-v6 / 2 - ((v6 / 2) ** 2 + (v5 / 3) ** 3) ** 0.5) ** (1.0 / 3)
        return 8 * int(math.ceil(v7 - v2 / (3 * v1)))
