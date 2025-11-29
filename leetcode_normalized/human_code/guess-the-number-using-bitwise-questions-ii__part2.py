from functools import reduce

class C1(object):

    def findNumber(self):
        """
        """
        v1 = 30
        return reduce(lambda accu, i: accu | (1 << i if commonBits(1 << i) - commonBits(1 << i) == 1 else 0), range(v1), 0)
