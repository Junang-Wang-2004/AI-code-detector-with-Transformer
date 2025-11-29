import itertools
from functools import reduce

class C1(object):

    def getSneakyNumbers(self, a1):
        """
        """

        def f(a1):
            return reduce(lambda accu, x: accu ^ x, (x for v1 in itertools.chain(a1, range(n)) if a1(v1)), 0)
        v1 = len(a1) - 2
        v2 = f(lambda _: True)
        v3 = v2 & -v2
        return [f(lambda x: x & v3 == 0), f(lambda x: x & v3 != 0)]
