from functools import reduce
# Time:  O(n)
# Space: O(1)

# array
class Solution(object):
    def doesValidArrayExist(self, derived):
        """
        """
        return reduce(lambda total, x: total^x, derived, 0) == 0
