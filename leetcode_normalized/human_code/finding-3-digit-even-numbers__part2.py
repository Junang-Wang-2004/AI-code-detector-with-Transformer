import collections
from functools import reduce

class C1(object):

    def findEvenNumbers(self, a1):
        """
        """
        v1, v2 = ([], collections.Counter(a1))
        for v3 in range(1, 10):
            for v4 in range(10):
                for v5 in range(0, 10, 2):
                    if v2[v3] > 0 and v2[v4] > (v4 == v3) and (v2[v5] > (v5 == v3) + (v5 == v4)):
                        v1.append(v3 * 100 + v4 * 10 + v5)
        return v1
