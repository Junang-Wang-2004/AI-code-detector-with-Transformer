# Time:  O(n^2)
# Space: O(n^2)
import collections


# freq table
class Solution2(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        """
        cnt = collections.Counter(x for row in grid for x in row)
        return [next(k for k, v in cnt.items() if v == 2), next(x for x in range(1, len(grid)**2+1) if x not in cnt)]
