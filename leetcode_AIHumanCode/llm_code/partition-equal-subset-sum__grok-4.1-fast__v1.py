class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        reachable = {0}
        for val in nums:
            reachable |= {prior + val for prior in reachable}
        return target in reachable
