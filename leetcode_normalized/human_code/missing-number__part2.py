import operator
from functools import reduce

class C1(object):

    def missingNumber(self, a1):
        return sum(range(len(a1) + 1)) - sum(a1)
