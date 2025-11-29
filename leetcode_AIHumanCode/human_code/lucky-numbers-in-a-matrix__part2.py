# Time:  O(m * n)
# Space: O(m + n)
import itertools


class Solution2(object):
    def luckyNumbers (self, matrix):
        """
        """
        return list(set(map(min, matrix)) &
                    set(map(max, zip(*matrix))))
 
