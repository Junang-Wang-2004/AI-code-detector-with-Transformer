# Time:  O(n^2)
# Space: O(n^2)
class Solution2(object):
    def __init__(self):
        self.__lookup = {(0, 0):0, (1, 1):2, (1, 0):3}  # special cases

    def minKnightMoves(self, x, y):
        """
        """
        def dp(x, y):
            x, y = abs(x), abs(y)
            if x < y:
                x, y = y, x
            if (x, y) not in self.__lookup:  # greedy, smaller x, y is always better if not special cases
                self.__lookup[(x, y)] = min(dp(x-1, y-2), dp(x-2, y-1)) + 1
            return self.__lookup[(x, y)]
        return dp(x, y)
