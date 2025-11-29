import math

class C1(object):

    def reachNumber(self, a1):
        """
        """
        a1 = abs(a1)
        v2 = int(math.ceil((-1 + math.sqrt(1 + 8 * a1)) / 2))
        a1 -= v2 * (v2 + 1) / 2
        return v2 if a1 % 2 == 0 else v2 + 1 + v2 % 2
