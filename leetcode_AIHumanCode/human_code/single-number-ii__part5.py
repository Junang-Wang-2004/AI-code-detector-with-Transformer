# Time:  O(n)
# Space: O(1)

import collections


class SolutionEX(object):
    # @param A, a list of integer
    # @return an integer
    # [1, 1, 1, 1, 2, 2, 2, 2, 3, 3]
    def singleNumber(self, A):
        one, two, three = 0, 0, 0
        for x in A:
            one, two, three = (~x & one) | (x & ~one & ~two & ~three), (~x & two) | (x & one), (~x & three) | (x & two)
        return two

