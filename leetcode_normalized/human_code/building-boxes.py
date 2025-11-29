import math

class C1(object):

    def minimumBoxes(self, a1):
        """
        """
        v1 = int((6 * a1) ** (1.0 / 3))
        if v1 * (v1 + 1) * (v1 + 2) > 6 * a1:
            v1 -= 1
        a1 -= v1 * (v1 + 1) * (v1 + 2) // 6
        v3 = int(math.ceil((-1 + (1 + 8 * a1) ** 0.5) / 2))
        return v1 * (v1 + 1) // 2 + v3
