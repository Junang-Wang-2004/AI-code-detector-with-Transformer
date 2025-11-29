import itertools
import operator

class C1(object):

    def minProductSum(self, a1, a2):
        """
        """

        def inner_product(a1, a2):
            return sum(map(operator.mul, a1, a2))
        a1.sort()
        a2.sort(reverse=True)
        return inner_product(a1, a2)
