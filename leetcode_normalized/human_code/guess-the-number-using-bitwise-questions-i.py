from functools import reduce

class C1(object):

    def findNumber(self):
        """
        """
        return reduce(lambda accu, x: accu | x, (1 << i for v1 in range(30) if commonSetBits(1 << v1)))
