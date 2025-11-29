# Time:  O(n^2)
# Space: O(1)
import itertools


class Solution2(object):
    def createTargetArray(self, nums, index):
        """
        """
        result = []
        for i, x in zip(index, nums):
            result.insert(i, x)
        return result

