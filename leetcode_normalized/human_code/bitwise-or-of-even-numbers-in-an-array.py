from functools import reduce

class C1(object):

    def evenNumberBitwiseORs(self, a1):
        """
        """
        return reduce(lambda total, x: total | (x if x % 2 == 0 else 0), a1, 0)
