# Time:  O(nlogn)
# Space: O(n)
import bisect


class Solution2(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        """
        sorted_nums = sorted(nums)
        return [bisect.bisect_left(sorted_nums, i) for i in nums]
