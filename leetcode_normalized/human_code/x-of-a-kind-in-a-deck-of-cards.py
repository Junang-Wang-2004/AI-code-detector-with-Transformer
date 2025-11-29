import collections
from functools import reduce

class C1(object):

    def hasGroupsSizeX(self, a1):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v1 = list(collections.Counter(a1).values())
        return reduce(gcd, v1) >= 2
