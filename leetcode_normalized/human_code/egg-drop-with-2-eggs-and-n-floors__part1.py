import math

class C1(object):

    def twoEggDrop(self, a1):
        """
        """
        return int(math.ceil((-1 + (1 + 8 * a1) ** 0.5) / 2))
