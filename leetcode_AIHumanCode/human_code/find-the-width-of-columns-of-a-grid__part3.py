# Time:  O(m * n)
# Space: O(m + logr)
import itertools


# array
class Solution3(object):
    def findColumnWidth(self, grid):
        """
        """
        return [max(len(str(x)) for x in col) for col in zip(*grid)]
