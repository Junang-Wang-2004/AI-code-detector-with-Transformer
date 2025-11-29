import operator
import collections
from functools import reduce

class C1(object):

    def findTheDifference(self, a1, a2):
        """
        """
        return chr(reduce(operator.xor, list(map(ord, a1)), 0) ^ reduce(operator.xor, list(map(ord, a2)), 0))

    def findTheDifference2(self, a1, a2):
        """
        """
        a2 = list(a2)
        a1 = list(a1)
        for v3 in a1:
            a2.remove(v3)
        return a2[0]

    def findTheDifference3(self, a1, a2):
        return chr(reduce(operator.xor, list(map(ord, a1 + a2))))

    def findTheDifference4(self, a1, a2):
        return list(collections.Counter(a2) - collections.Counter(a1))[0]

    def findTheDifference5(self, a1, a2):
        a1, a2 = (sorted(a1), sorted(a2))
        return a2[-1] if a1 == a2[:-1] else [x[1] for v3 in zip(a1, a2) if v3[0] != v3[1]][0]
