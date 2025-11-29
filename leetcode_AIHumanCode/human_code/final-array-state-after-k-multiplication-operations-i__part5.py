# Time:  O(k * n)
# Space: O(1)
# simulation
class Solution5(object):
    def getFinalState(self, nums, k, multiplier):
        """
        """
        if multiplier == 1:
            return nums
        for _ in range(k):
            i = min(range(len(nums)), key=lambda i: nums[i])
            nums[i] *= multiplier
        return nums
