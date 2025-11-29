import operator
import collections
from functools import reduce

class C1(object):

    def singleNumber(self, a1):
        """
        """
        return [x[0] for v1 in sorted(list(collections.Counter(a1).items()), key=lambda i: i[1], reverse=False)[:2]]
