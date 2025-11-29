# Time:  O(n * logr)
# Space: O(logr), r = max(nums)
# array
class Solution2(object):
    def separateDigits(self, nums):
        """
        """
        return [int(c) for x in nums for c in str(x)]
