from functools import reduce

class C1(object):

    def maximumXOR(self, a1):
        """
        """
        return reduce(lambda x, y: x | y, a1)
