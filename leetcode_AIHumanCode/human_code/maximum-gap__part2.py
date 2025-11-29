# Time:  O(nlogn)
# Space: O(n)
class Solution2(object):
    def maximumGap(self, nums):
        """
        """

        if len(nums) < 2:
            return 0

        nums.sort()
        pre = nums[0]
        max_gap = float("-inf")

        for i in nums:
            max_gap = max(max_gap, i - pre)
            pre = i
        return max_gap


