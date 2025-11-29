from functools import reduce

class C1(object):

    def doesValidArrayExist(self, a1):
        """
        """
        return reduce(lambda total, x: total ^ x, a1, 0) == 0
