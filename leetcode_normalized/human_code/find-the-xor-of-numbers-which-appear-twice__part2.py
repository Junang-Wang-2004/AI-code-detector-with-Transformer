import collections
from functools import reduce

class C1(object):

    def duplicateNumbersXOR(self, a1):
        """
        """
        return reduce(lambda x, y: x ^ y, (x for v1, v2 in collections.Counter(a1).items() if v2 == 2), 0)
