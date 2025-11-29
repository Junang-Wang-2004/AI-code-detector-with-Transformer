import math

class C1(object):

    def arrangeCoins(self, a1):
        """
        """
        return int((math.sqrt(8 * a1 + 1) - 1) / 2)
