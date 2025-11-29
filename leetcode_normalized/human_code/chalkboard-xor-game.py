from operator import xor
from functools import reduce

class C1(object):

    def xorGame(self, a1):
        """
        """
        return reduce(xor, a1) == 0 or len(a1) % 2 == 0
