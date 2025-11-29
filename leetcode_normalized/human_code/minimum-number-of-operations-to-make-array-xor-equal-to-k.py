from functools import reduce

class C1(object):

    def minOperations(self, a1, a2):
        """
        """

        def popcount(a1):
            return bin(a1).count('1')
        return popcount(reduce(lambda x, y: x ^ y, a1, a2))
